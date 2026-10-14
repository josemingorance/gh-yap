# Regenerate with: vhs assets/demo.es.tape  (point GH_YAP_REPO at your own sandbox repo)
Output assets/demo.es.gif
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
Env GH_YAP_LANG "es"

Type "gh yap feed -n 3" Sleep 300ms Enter Sleep 3.5s
Type 'gh yap post "desplegando en viernes, ¿qué puede salir mal? #yolo"' Sleep 300ms Enter Sleep 2.5s
Type "gh yap like 5" Sleep 300ms Enter Sleep 1.5s
Type 'gh yap reply 5 "yo también, sin café no compilo"' Sleep 300ms Enter Sleep 2s
Type "clear" Enter
Type "gh yap view 5" Sleep 300ms Enter Sleep 5s
