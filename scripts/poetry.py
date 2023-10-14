import os
import platform
import re
import shutil
import sys
import typing as t
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

if platform.system() == "Windows":
    os.environ["COMSPEC"] = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
    IS_WINDOWS = True
else:
    IS_WINDOWS = False

ROOT_DIR = Path(__file__).parent.parent
SERVER_DIR = ROOT_DIR / "server"
TEST_DIR = ROOT_DIR / "tests"
SOURCE_DIR = (SERVER_DIR, TEST_DIR)
CMD_START = "$"


def make_prefix(envs):
    e = envs or dict()
    if platform.system() == "Windows":
        return "".join([f"$env:{k} = '{str(v)}'; " for k, v in e.items()])
    else:
        return "".join([f"{k}={str(v)} " for k, v in e.items()])


def list_all_dirs_files() -> t.Tuple[t.List[str], t.List[str]]:
    listdirs = []
    listfiles = []
    for root, subdirs, files in os.walk(os.getcwd()):
        listfiles += [os.path.join(root, f) for f in files]
        listdirs += [os.path.join(root, s) for s in subdirs]
    return listdirs, listfiles


def run_pycacheremove():
    regex_success = re.compile(r"__pycache__")
    regex_deny = re.compile(r"(\.venv)|(scripts)")
    dirs, _ = list_all_dirs_files()
    count = 0
    for d in dirs:
        if not regex_deny.search(d) and regex_success.search(d):
            try:
                shutil.rmtree(d)
                print(f"{d}:", "removed")
                count += 1
            except Exception as err:
                print(f"{d}:", str(err))
    print(f"{count} '__pycache__' folders have been removed!")


def run_shell(command: str):
    print(f"{CMD_START} {command!s}")
    os.system(command)


def run_server():
    run_redis_start()
    run_shell("FLASK_APP=server.web flask run --host=0.0.0.0 --port=5000 --debug")


def run_worker():
    run_redis_start()
    cmd = " ".join(
        [
            "watchmedo auto-restart --directory=./server --pattern=*.py --recursive --",
            "celery -A server.worker worker --concurrency=2 -B --loglevel=INFO -E",
        ]
    )
    run_shell(cmd)


def run_flower():
    run_redis_start()
    run_shell("celery -A server.worker flower --address='localhost' --port=5555")


def run_makerequirements():
    run_shell(
        "poetry export -f requirements.txt --without-hashes --output requirements.txt"
    )


def run_format():
    src = " ".join([str(src) for src in SOURCE_DIR])
    run_shell(f"ruff check --fix {src!s}")


def run_lint():
    src = " ".join([str(src) for src in SOURCE_DIR])
    run_shell(f"ruff check {src!s}")
    run_shell(f"mypy {src!s}")


def run_pyshell():
    run_shell("python ipython")


def run_test():
    prefix = make_prefix({"PYTHONDONTWRITEBYTECODE": "1"})
    run_shell(prefix + "pytest -vv --durations=0 ")


def run_precommit():
    run_lint()
    run_test()


def run_redis_start():
    cmd = "cd ./docker && docker compose -f redis.yaml up -d"
    run_shell(cmd)


def run_redis_stop():
    cmd = "cd ./docker && docker compose -f redis.yaml stop"
    run_shell(cmd)


def run_redis_down():
    cmd = "cd ./docker && docker compose -f redis.yaml down -v"
    run_shell(cmd)


def run_redis_clean():
    cmd = (
        "cd ./docker && "
        "docker compose -f redis.yaml down -v && "
        "docker compose -f redis.yaml up -d"
    )
    run_shell(cmd)


def run_redis_log():
    cmd = "cd ./docker && docker compose -f redis.yaml logs -f"
    run_shell(cmd)


if __name__ == "__main__":
    sys.exit(1)
