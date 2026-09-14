"""仅在启动和迁移时导入所有模块模型；业务代码仍由各模块所有。"""

from app.shared.platform.models import *  # noqa: F403
from app.shared.security.authorization.models import *  # noqa: F403
from app.shared.security.identity.models import *  # noqa: F403
