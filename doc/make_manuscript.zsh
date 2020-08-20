#! /bin/zsh
#

output=./output
FAST="N"

for i in "$@"
do
case $i in
    -f|--fast)
    FAST="Y"
    shift # past argument=value
    ;;
    *)
          # unknown option
    ;;
esac
done

# Generates a document with question marks in place of unknown references and references stored in the aux file in the form of arguments that were supplied to \cite commands.
pdflatex -shell-escape -output-directory=$output -jobname=casq2_manuscript_figures manuscript.tex | tee $output/1_pdflatex.log

if [ "$FAST" = "Y" ]; then
    echo "Exiting early per request. No references will be built."
else
    # Read the aux file and produce a formatted bibliography.
    # bibtex ./output/manuscript_with_refs.aux
    bibtex $output/casq2_manuscript_figures.aux | tee $output/2_bibtex.log

    # Now that the bibliography exists, it will be added to the main document on this run. Also on this run, the correct citation labels will be written to the aux file.
    pdflatex -shell-escape -output-directory=$output -jobname=casq2_manuscript_figures manuscript.tex | tee $output/3_pdflatex.log

    # Regenerate the document again, this time using the correct citation labels from the aux file.
    pdflatex -shell-escape -output-directory=$output -jobname=casq2_manuscript_figures manuscript.tex | tee $output/4_pdflatex.log
fi

# View
open $output/casq2_manuscript_figures.pdf




# output=$1

# pdflatex -shell-escape -output-directory=$output -jobname=CASQ2_Manuscript_Figures_Only manuscript.tex | tee $output/1_pdflatex.log

# # View
# open $output/CASQ2_Manuscript_Figures_Only.pdf

# # mkdir -p output

# # pdflatex -shell-escape -output-directory=./output -jobname=CASQ2_Manuscript_Figures_Only manuscript.tex

# # # pdflatex -shell-escape -output-directory=./output -jobname=manuscript_no_refs manuscript.tex

# # # View
# # open ./output/CASQ2_Manuscript_Figures_Only.pdf

# cp ./output/CASQ2_Manuscript_Figures_Only.pdf ../target/biorxiv/CASQ2_Manuscript_Figures_Only.pdf

# pdfjam "../target/biorxiv/CASQ2 Manuscript_2020_01_01_ET_Edits_No_Comments.pdf" '1-34,41-45' ../target/biorxiv/CASQ2_Manuscript_Figures_Only.pdf "../target/biorxiv/Supplemental Material_2020-01-01_Table_1_Added_ET.pdf" --outfile "../target/biorxiv/CASQ2_Manuscript_Text_And_Figures.pdf"