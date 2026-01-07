"""
python-invoke tasks to run the Antora site generator.
"""

from invoke import context, task

BUILD_DIR = 'build/'
ANTORA_PLAYBOOK = 'antora-playbook.yml'

def ctx_run(
  ctx: context,
  cmd: list[str],
) -> None:
  """
  Boiler plate function to
  flatten the command list
  and run the command.
  """
  ctx.run(' '.join(cmd))

@task
def clean(
  ctx: context,
) -> None:
  """
  Clean the build directory.
  """
  ctx_run(
    ctx,
    [
      'rm',
      '-rf',
      BUILD_DIR,
    ],
  )

@task
def build(
  ctx: context,
) -> None:
  """
  Build the Antora site.
  """
  ctx_run(
    ctx,
    [
      'antora',
      ANTORA_PLAYBOOK,
    ],
  )
