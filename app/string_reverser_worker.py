from conductor.client.http.models import Task, TaskResult
from conductor.client.http.models.task_result_status import TaskResultStatus
from conductor.client.worker.worker_interface import WorkerInterface
from string_reverser import StringReverser

class StringReverserWorker(WorkerInterface):
    def execute(self, task: Task) -> TaskResult:
        task_result = self.get_task_result_from_task(task)
        input = task.input_data['input']['result']
        reverse = StringReverser.reverse_string(input)
        task_result.add_output_data('reverse', reverse)
        task_result.status = TaskResultStatus.COMPLETED
        return task_result

    def get_polling_interval_in_seconds(self) -> float:
        # poll every 10s
        return 10