# Regenerate with: vhs assets/demo.tape  (point GH_YAP_REPO at your own sandbox repo)
Output assets/demo.gif
Set Shell "bash"
Set FontSize 20
Set Width 1200
Set Height 760
Set Padding 28
Set Theme "Catppuccin Mocha"
Set WindowBar Colorful
Set BorderRadius 12
Set TypingSpeed 45ms
Env GH_YAP_REPO "josemingorance/yap-demo"
Env GH_NO_UPDATE_NOTIFIER "1"
Env GH_YAP_LANG "en"

Type "gh yap feed -n 3" Sleep 300ms Enter Sleep 3.5s
Type 'gh yap post "shipping on a friday. what could go wrong? #yolo"' Sleep 300ms Enter Sleep 2.5s
Type "gh yap like 6" Sleep 300ms Enter Sleep 1.5s
Type 'gh yap reply 6 "you got this @josemingorance"' Sleep 300ms Enter Sleep 2s
Type "clear" Enter
Type "gh yap view 6" Sleep 300ms Enter Sleep 5s
