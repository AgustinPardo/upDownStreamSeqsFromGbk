#!/bin/bash

form=$(zenity --forms --title "Welcome to UpDownStreamFromGbk output parser" --text  "" \
--add-entry "Fasta input" \
--add-entry "Fasta ouput name")
[[ "$?" != "0" ]] && exit 1

# extract the IP and DRIVE values
input=$(awk -F'|' '{print $1}' <<<$form);    
output=$(awk -F'|' '{print $2}' <<<$form);

echo $output

zenity --text-info --width 800 --height 700 --timeout=60 --filename="$input" --title "Look your input file"
[[ "$?" != "0" ]] && exit 1

ListType=`zenity --width=800 --height=300 --list --radiolist \
     --title '' \
     --text 'Select the commnad to apply:' \
     --column 'Select' \
     --column 'Scan Type' --column 'info' \
      TRUE "Comando1" "Extended fasta" FALSE "Comando2" "Original fasta" FALSE "Comando3" "Upstream extention" FALSE "Comando4" "Downstream extention"`

if [[ $?  != "0" ]]; then
  exit 1 
elif [ $ListType == "Comando1" ]; then
  result=$(awk '0 == (NR+1) % 4, 0 == (NR) % 4' < $input);
  echo  "$result" > $output
  zenity --text-info --width 800 --height 700 --filename=$output --title "Look your output file"
  if [[ $?  != "0" ]]; then rm $output; fi
elif [ $ListType == "Comando2" ]; then
  result=$(awk '0 == (NR-1) % 4,0 == (NR-2) % 4' < $input);
  echo  "$result" > $output
  zenity --text-info --width 800 --height 700  --filename=$output --title "Look your output file"
  if [[ $?  != "0" ]]; then rm $output; fi
elif [ $ListType == "Comando3" ]; then
  extention=$(zenity --entry --text "How much to take from upstream?" --title "" --entry-text="");
  [[ "$?" != "0" ]] && exit 1
  result=$(awk '{if (/^>/) print $0; else print(substr($1,1,'$extention')) }'< $input);
  echo  "$result" > $output
  zenity --text-info --width 800 --height 700  --filename=$output --title "Look your output file"
  if [[ $?  != "0" ]]; then rm $output; fi
elif [ $ListType == "Comando4" ]; then
  extention=$(zenity --entry --text "How much to take from downstream?" --title "" --entry-text="");
  [[ "$?" != "0" ]] && exit 1
  result=$(awk '{if (/^>/) print $0; else print(substr($1, length($1)-100, length($1))) }'< $input);
  echo  "$result" > $output
  zenity --text-info --width 800 --height 700 --filename=$output --title "Look your output file"
  if [[ $?  != "0" ]]; then rm $output; fi
fi
