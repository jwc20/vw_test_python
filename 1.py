import vowpal_wabbit_next as vw
import io

cb_input = io.StringIO(
    """shared | s
0:1:0.5 | a=0
| a=1

shared | s
| a=0
1:0:0.5 | a=1"""
)

workspace = vw.Workspace(["--cb_explore_adf"])

with vw.TextFormatReader(workspace, cb_input) as reader:
    for event in reader:
        print(workspace.predict_then_learn_one(event))
