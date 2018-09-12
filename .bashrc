# Simple version of prompt string
#export PS1="\w $ "

# Fancy tmux version of prompt string?
# create a global per-pane variable that holds the pane's PWD
export PS1=$PS1'$( [ -n $TMUX ] && tmux setenv -g TMUX_PWD_$(tmux display -p "#D" | tr -d %) $PWD)'
