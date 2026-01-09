from pathlib import Path
import subprocess

REPO_ROOT = Path(__file__).resolve().parents[2]

print(REPO_ROOT)
PHASE_A_ENTRY = REPO_ROOT / "scripts" / "run_failure_aggregation_v1.sh"
EXP_DIR = REPO_ROOT / "phase_b" / "experiments" / "day16_call_test"
EXP_DIR.mkdir(parents = True, exist_ok = True)

proc = subprocess.run(
    ["bash", str(PHASE_A_ENTRY)],
    input = b"2.0\n",
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
    cwd = str(REPO_ROOT),
)

print("returncode: ", proc.returncode)
(EXP_DIR / "returncode.txt").write_text(str(proc.returncode))
(EXP_DIR / "stdout.txt").write_bytes(proc.stdout)
(EXP_DIR / "stderr.txt").write_bytes(proc.stderr)