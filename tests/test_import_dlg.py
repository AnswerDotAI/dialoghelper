import asyncio
from unittest.mock import AsyncMock, patch

import dialoghelper.core as core


def test_import_dlg_routes_target():
    msg = dict(content='test', msg_type='note')
    with patch.object(core, 'find_msgs', AsyncMock(return_value=[msg])), patch.object(core, 'add_msg', AsyncMock(return_value='_id')) as add:
        assert asyncio.run(core.import_dlg('/src', dname='/tmp')) == ['_id']
        assert add.await_args.kwargs['dname'] == '/tmp'
