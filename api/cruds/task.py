from typing import List, Tuple, Optional

async def get_task(db: AsyncSession, task_id: int) -> Optional[task_model.Task]:
  result: Result = await db.execute(
    select(task_model.Task).filter(task_model.Task.id == task_id)
  )
  task: Optional[Tuple[task_model.Task]] = result.first()
  return task[0] if task is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す

async def update_task(
  db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
) -> task_model.Task:
  original.title = task_create.title
  db.add(original)
  await db.commit()
  await db.refresh(original)
  return original

async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
  await db.delete(original)
  await db.commit()
