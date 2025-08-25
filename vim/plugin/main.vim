let s:buffers=[]
let s:lines=[]
let s:main_buffer_id=-1
let s:current_log_no=-1
let g:lolog_pattern='*'

function! s:loadLog(dirname)
    if !isdirectory(a:dirname)
        echoerr a:dirname . ' is not a valid directory'
        return
    endif
    let entries=globpath(a:dirname,g:lolog_pattern,0,1)
    let file_names=filter(entries,'!isdirectory(v:val)')
    sort(file_names)
    let s:lines=[]
    for fname in file_names
        echo 'load content from ' . fname
        let s:lines+=readfile(fname)
    endfor
    let s:lines=map(s:lines,'[v:key+1,v:val]')
endfunction

function! s:addView(regexp)
    let new_buf_no=bufnr('lolog search: ' . a:regexp,1)
    call setbufvar(new_buf_no,'&hidden',1)
    call setbufvar(new_buf_no,'&buftype','nofile')
    call setbufvar(new_buf_no,'&filetype','lolog_view')
    call add(s:buffers,new_buf_no)
    execute new_buf_no . 'buffer'
    for [no,content] in s:lines
        if content =~ a:regexp
            call append('$',no . ' ' . content)
        endif
    endfor
    execute '1d'
endfunction

function! s:clear()
    let s:lines=[]
    let s:main_buffer_id=-1
    let s:current_log_no=-1
    for i in buffers
        execute 'bdelete ' . i
    endfor
endfunction

command! -nargs=1 LologLoad call <SID>loadLog("<args>")
command! -nargs=1 LologAddView call <SID>addView("<args>")
command! LologClear call <SID>clear()
