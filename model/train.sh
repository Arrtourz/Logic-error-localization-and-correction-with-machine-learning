#name="code-compiler--no-graph"
#mkdir -p out_spoc/${name}
#python3 -u main_spoc.py -o ${name} train \
#    configs/base.yml  configs/data-spoc/err-data-orig.yml \
#    configs/model-code-compiler/no-graph--dec-attn-all.yml \
#    > out_spoc/${name}/log.txt 2>&1

#name="code-only"
#mkdir -p out_spoc/${name}
#python3 -u main_spoc.py -o ${name} train \
#    configs/base.yml  configs/data-spoc/err-data-orig.yml \
#    configs/model-code-only/no-graph--dec-attn-all.yml \
#    > out_spoc/${name}/log.txt 2>&1

#name="code-compiler-text--2l-graph--finetune"
#mkdir -p out_spoc/${name}
#python3 -u main_spoc.py -o ${name} train \
#    -l out_spoc/code-compiler--2l-graph--pretrain/400000-add_text \
#    configs/base.yml  configs/data-spoc/err-data-orig-finetune.yml \
#    configs/model-code-compiler-text/2l-graph.yml \
#    > out_spoc/${name}/log.txt 2>&1

#name="code--graph"
#mkdir -p out_spoc/${name}
#python3 -u main_spoc.py -o ${name} train \
#    configs/base.yml  configs/data-spoc/err-data-orig.yml \
#    configs/model-code-compiler/2l-graph--dec-attn-all.yml \
#    > out_spoc/${name}/log.txt 2>&1

name="code--text"
mkdir -p out_spoc/${name}
python3 -u main_spoc.py -o ${name} train \
    configs/base.yml  configs/data-spoc/err-data-orig.yml \
    configs/model-code-compiler-text/2l-graph.yml \
    > out_spoc/${name}/log.txt 2>&1

