#definiert das Aussehen aller Widgets
#legt directories an, auf die global zugegriffen werden kann -> Widgets ziehen sich die Einstellungen

Schriftart = "DejaVu Sans" #"Cooperplate Gothic Medium"
großeSchrift = 18
mittlereSchrift = 15
normaleSchrift = 10

hintergrund = "#5778E8"
schriftfarbe = "black"
überschriftfarbe = "#F2DF1F"

buttonfarbeButton = "#F2DF1F"
buttonfarbeSchrift = "#400000"
buttonfarbeButtonHoverBack = "#400000"
buttonfarbeButtonHoverFor = "#F2DF1F"

aussehenButton = {"font": (Schriftart, normaleSchrift), "bg": buttonfarbeButton, "fg": buttonfarbeSchrift, "activebackground": buttonfarbeButtonHoverBack, "activeforeground": buttonfarbeButtonHoverFor}
aussehenLabel = {"font": (Schriftart, normaleSchrift), "bg": hintergrund, "fg": schriftfarbe} #normale Schrift zwischendrin
aussehenLabelGroß = {"font": (Schriftart, mittlereSchrift), "bg": hintergrund, "fg": schriftfarbe} #normale Schrift zwischendrin
aussehenLabelÜberschrift = {"font": (Schriftart, großeSchrift), "bg": hintergrund, "fg": überschriftfarbe} #große Überschrift über Bildschirm
aussehenLabelÜberschriftKlein = {"font": (Schriftart, normaleSchrift), "bg": hintergrund, "fg": überschriftfarbe} #kleine Überschrift über Bildschirm
aussehenRadio = {"font": (Schriftart, normaleSchrift), "bg": hintergrund, "fg": schriftfarbe, "activebackground": buttonfarbeButtonHoverFor}
aussehenEntry = {"font": (Schriftart, normaleSchrift), "bg": "white", "fg": schriftfarbe, "insertbackground": schriftfarbe} # insertbackground = Cursorfarbe
aussehenScale = {"font": (Schriftart, normaleSchrift), "bg": hintergrund, "fg": schriftfarbe, "troughcolor": "grey", "highlightthickness": 0}  # troughcolor = Farbe der Schiene
aussehenFrame = {"bg": hintergrund, "highlightthickness": 0}
aussehenCanvas = {"bg": hintergrund, "highlightthickness": 0}
aussehenFenster = {"bg" : hintergrund, "highlightthickness": 0}
aussehenScrollbar = {"bg": hintergrund, "troughcolor": hintergrund, "activebackground": "darkgrey"}

#"highlightthickness": 0 --> kein Rand