from dataclasses import dataclass
import sqlite3
from typing import Any

from .authorized_operator_storage import AuthorizedOperatorStorageMixin
from .base import BaseStore
from .common import MutationResult, ValidationResult
from .environment_contract import EnvironmentContractMixin
from .environment import EnvironmentEvidenceMixin
from .execution import ExecutionMixin
from .helper_recovery_lineage import HelperRecoveryLineageMixin
from .integrity import ExecutionIntegrityMixin
from .integrity_scope import ExecutionScopeHardeningMixin
from .observability import ObservabilityMixin
from .operational_learning_storage import OperationalLessonStorageMixin
from .outcomes import OutcomeMixin
from .policy import PolicyStateMixin
from .readiness import ReadinessMixin
from .release_check import ReleaseCheckMixin
from .review import ReviewMixin
from .review_binding import ReviewBindingMixin
from .run_lineage import RunSessionLineageMixin
from .run_lineage_trace import RunSessionTraceMixin
from .skill_lifecycle_storage import SkillLifecycleStorageMixin
from .submission_lineage import SubmissionRunLineageMixin


class TaskStore(
    RunSessionTraceMixin,
    ExecutionScopeHardeningMixin,
    AuthorizedOperatorStorageMixin,
    SkillLifecycleStorageMixin,
    OperationalLessonStorageMixin,
    HelperRecoveryLineageMixin,
    SubmissionRunLineageMixin,
    RunSessionLineageMixin,
    ExecutionIntegrityMixin,
    EnvironmentContractMixin,
    EnvironmentEvidenceMixin,
    PolicyStateMixin,
    ReadinessMixin,
    ExecutionMixin,
    ReviewBindingMixin,
    ReviewMixin,
    ReleaseCheckMixin,
    OutcomeMixin,
    ObservabilityMixin,
    BaseStore,
):
    """Canonical SQLite task store for MAPS Lean."""

    def task_waits(self, task_id: str) -> dict[str, object] | None:
        """Derive an operator wait report from one consistent task snapshot."""
        from runtime.wait_projection import project_task_waits

        with self._read_snapshot() as conn:
            return project_task_waits(_TaskReadSnapshot(self, conn), task_id)


@dataclass(frozen=True)
class _TaskReadSnapshot:
    store: TaskStore
    conn: sqlite3.Connection

    def get_task(self, task_id: str) -> dict[str, Any] | None:
        return self.store._get_task(self.conn, task_id)

    def list_reviews(self, task_id: str) -> list[dict[str, Any]]:
        return self.store._list_reviews(self.conn, task_id)


__all__ = ["MutationResult", "TaskStore", "ValidationResult"]
