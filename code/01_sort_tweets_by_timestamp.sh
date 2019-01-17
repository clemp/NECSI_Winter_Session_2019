cd ../data
# awk '{ gsub(/[a-zA-Z]/,"", $3)}' higgs-activity_time_sample.txt > higgs-activity_time_sample_clean.txt
# sort -nk3 higgs-activity_time_sample_clean.txt > higgs-activity_time_sample_clean_sorted.txt
sort -nk3 higgs-activity_time.txt > higgs-activity_time_sorted.txt

grep RT higgs-activity_time_sorted.txt > higgs-activity_time_sorted_RT.txt
