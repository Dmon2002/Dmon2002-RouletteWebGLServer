[phases.setup]
nixPkgs = ['python311', 'pip', 'gcc', 'libffi', 'openssl']

[phases.install]
cmds = ['pip install --upgrade pip', 'pip install -r requirements.txt']
