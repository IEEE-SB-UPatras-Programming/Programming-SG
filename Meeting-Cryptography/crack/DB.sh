for p in $(cat passwords.txt | shuf | head -n 500)
do
    RND_NAME=$(cat /usr/share/dict/words | shuf -n 1)
    HSH_PASSWORD=$(echo $p | sha256sum)
    echo $HSH_PASSWORD $RND_NAME >> challenge/DB
    echo $p - $RND_NAME >> challenge/DB.solution
done
