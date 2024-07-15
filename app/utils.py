import logging

from .routers import socketio as socketio_router, xlwings as xlwings_router

logger = logging.getLogger(__name__)


async def trigger_script(script, **options):
    sid = xlwings_router.socketio_id_context.get()
    if not isinstance(script, str):
        script = script.__name__
    await socketio_router.sio.emit(
        "xlwings:trigger-script",
        {"script_name": script, "config": options},
        to=sid,
    )
    logger.info(f"Script '{script}' triggered for sid '{sid}' with config: {options}")
