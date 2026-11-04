import asyncio, json
import pytest
from dialoghelper import cells_client, update_msg, toggle_export, read_msg, add_msgs, del_msgs, msg_str_replace
from fasttransport.errors import APIError

RUN = r'from test_core import check_message_edits; await check_message_edits()'


async def check_message_edits():
    "Revise recorded messages, then edit and delete an ordered batch with one audit note"
    fc = cells_client()
    outs = [dict(output_type='stream', name='stdout', text='kept')]
    await fc.apply([dict(op='add', cell=dict(id='target', cell_type='code', source='1', outputs=outs,
        execution_count=7, metadata=dict(skipped=True, pinned=True, nested=dict(a=1))))])

    await update_msg('target', content='2', mergemeta=dict(nested=dict(b=2)))
    c, = await fc.cells(ids='target')
    assert c['source']=='2' and c['outputs']==outs and c['execution_count']==7
    assert c['metadata']['nested']==dict(a=1,b=2) and c['metadata']['pinned']

    await update_msg('target', meta=dict(fresh=True), mergemeta=dict(nested=dict(c=3)))
    c, = await fc.cells(ids='target')
    assert c['metadata']==dict(fresh=True, nested=dict(c=3))

    await update_msg('target', msg_type='code')
    c, = await fc.cells(ids='target')
    assert c['outputs']==outs and c['execution_count']==7

    await update_msg('target', msg_type='note')
    c, = await fc.cells(ids='target')
    assert c['cell_type']=='markdown' and 'outputs' not in c and 'execution_count' not in c
    await update_msg('target', output='reply', msg_type='prompt')
    assert (await read_msg(id='target', n=0))['output']=='reply'
    await update_msg('target', msg_type='code', output='[]', mergemeta=dict(nbdev=dict(exports='mymod', default_exp='core')))
    await toggle_export('target')
    c, = await fc.cells(ids='target')
    assert c['metadata']['nbdev']==dict(default_exp='core') and c['outputs']==[]

    with pytest.raises(ValueError, match='start_line'): await read_msg(id='target', n=0, start_line=0)
    with pytest.raises(APIError, match='missing'): await fc.apply([dict(op='merge', id='missing', metadata=dict(pinned=True))])

    ids = await add_msgs([dict(content='hello one'), dict(content='hello two', msg_type='code', output=json.dumps(outs), pinned=1)], msgid='target')
    before = {c['id'] for c in await fc.cells()}
    changes = await msg_str_replace([ids[0], 'missing', ids[1]], 'hello', 'hi', log_changed=True)
    assert changes[1] == ('missing', 'error: No message missing')
    cells = await fc.cells()
    assert [c['source'] for c in cells if c['id'] in ids] == ['hi one', 'hi two']
    c = next(c for c in cells if c['id']==ids[1])
    assert c['outputs']==outs and c['metadata']['pinned']
    logs = [c for c in cells if c['id'] not in before]
    assert len(logs)==1 and all(i in logs[0]['source'] for i in ids)

    before = {c['id'] for c in cells}
    assert await del_msgs(','.join(ids), log_changed=True) == ids
    cells = await fc.cells()
    logs = [c for c in cells if c['id'] not in before]
    assert not any(c['id'] in ids for c in cells) and len(logs)==1
    assert all(s in logs[0]['source'] for s in ('hi one', 'hi two'))


@pytest.mark.asyncio
async def test_message_edits(kernel):
    async with asyncio.timeout(30): reply = (await kernel.reply(RUN, metadata=dict(cellId='checks')))['content']
    assert reply['status']=='ok', '\n'.join(reply.get('traceback', [])) or reply
