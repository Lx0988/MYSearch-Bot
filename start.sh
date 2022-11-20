if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/0AIB/LxInline.git /LxInline
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /LxInline
fi
cd /LxInline
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 -m bot
