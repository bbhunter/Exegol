import hashlib
import platform
import uuid

from exegol.utils.ExeLog import logger
from exegol.utils.LocalDatastore import LocalDatastore


class MUID:

    @classmethod
    def __compute(cls, rid: str) -> str:
        uname = platform.uname()
        data = [rid,
                uname.processor,
                uname.machine,
                uname.version,
                uname.release,
                uname.system,
                uname.node,
                "/".join(platform.architecture())]
        return hashlib.sha3_256('+'.join(data).encode("utf-16")).hexdigest()

    @classmethod
    def get_current_muid(cls) -> str:
        logger.debug("Computing MUID")
        rid, mid = LocalDatastore().get_machine_id()
        if rid is not None:
            current_id = cls.__compute(rid)
            if mid == current_id:
                return current_id
        rid = str(uuid.uuid4())
        current_id = cls.__compute(rid)
        LocalDatastore().update_mid(rid, current_id)
        return current_id

    @classmethod
    def __generate_activation_id(cls) -> str:
        act_id = uuid.uuid4().hex[:8].upper()
        logger.debug(f"Generating activation ID: {act_id}")
        LocalDatastore().set(LocalDatastore.Key.ACTIVATION_ID, act_id)
        return act_id

    @classmethod
    def get_activation_id(cls) -> str:
        act_id = LocalDatastore().get_activation_id()
        if act_id is None:
            act_id = cls.__generate_activation_id()
        return act_id
