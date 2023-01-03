repo_root="../../../.."
program_data_root=${repo_root}"/raw_data/deepfix_data"
test_split_root=${repo_root}"/data/err-data-compiler--auto-corrupt--orig-deepfix/bin4"

name="code-compiler--2l-graph"
mkdir -p out/${name}/log
cd out/${name}

for entry in ${test_split_root}/*
do
  probid=`basename $entry`
  python3 -u ../../test_deepfix.py \
  --input-code-dir ${program_data_root}/${probid}/correct \
  --repairer-server  http://192.168.10.103:8080/pred
done
