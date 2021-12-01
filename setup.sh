mkdir -p ~/.streamlit/
echo "\
[theme]\n\
primaryColor = '#777'\n\
backgroundColor = '#00172B'\n\
secondaryBackgroundColor = '#0083B8'\n\
textColor = '#f9f9f9'\n\
font = 'monospace'\n\
\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml