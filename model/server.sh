name="SERVER--code-compiler--2l-graph--finetune"
mkdir -p out_spoc/${name}
python3 -u main_spoc.py -o ${name} server -p 8080 \
    -l out_spoc/code-compiler--2l-graph--finetune/550000 \
    configs/base.yml  configs/data-spoc/err-data-orig.yml \
    configs/model-code-compiler/2l-graph--dec-attn-all.yml

#name="SERVER--code-compiler-text--2l-graph--finetune"
#mkdir -p out_spoc/${name}
#python3 -u main_spoc.py -o ${name} server -p 8082 \
#    -l out_spoc/code-compiler-text--2l-graph--finetune/550000 \
#    configs/base.yml  configs/data-spoc/err-data-orig.yml \
#    configs/model-code-compiler-text/2l-graph.yml


#name="SERVER--code-compiler--no-graph"
#mkdir -p out_spoc/${name}
#python3 -u main_spoc.py -o ${name} server -p 8083 \
#    -l out_spoc/code-compiler--no-graph/15000 \
#    configs/base.yml  configs/data-spoc/err-data-orig.yml \
#    configs/model-code-compiler/no-graph--dec-attn-all.yml

#name="SERVER--code-only"
#mkdir -p out_spoc/${name}
#python3 -u main_spoc.py -o ${name} server -p 8083 \
#    -l out_spoc/code-only/15000 \
#    configs/base.yml  configs/data-spoc/err-data-orig.yml \
#    configs/model-code-only/no-graph--dec-attn-all.yml \
