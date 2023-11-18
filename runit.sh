# This script requires that OPENAI_API_KEY is set in ~/.zshrc
# shellcheck disable=SC1090
source ~/.zshrc
#echo "OPENAI_API_KEY="$OPENAI_API_KEY
python3 -m venv venv
. venv/bin/activate
#pip3 install -r requirements.txt
pip3 install --upgrade openai
clear
choices=('chat_completions.py' 'embeddings.py')

while true
do
  for (( i=0; i<"${#choices[@]}"; i++ ));
  do
    echo "$i." "${choices[$i]}"
  done
  echo "${#choices[@]}." "Quit"
  read -rp "Enter: "

  if [[ $REPLY -lt "${#choices[@]}" ]]
  then
    python3 "${choices[$REPLY]}"
  else
    break
  fi
done