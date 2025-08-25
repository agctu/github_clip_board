vim -c 'redir! > log' -c 'LologLoad .' -c 'LologAddView redir' -c 'echo getline(1,"$")' -c 'q!'
cat log
echo
