PRO test_ng_barplot_1

fig_sav = 0

months = [4:10];4+INDGEN(7)
data1 = [6, 11, 7, 14, 18, 9, 7]
data2 = [13, 10, 13, 7, 4, 10, 6]

win1 = WINDOW(DIMENSIONS=[800, 600], /NO_TOOLBAR)
bp = BARPLOT(months, data1, YRANGE=[0, 20], XTICKINTERVAL=1, XMINOR=0, $
  ;PATTERN_ORIENTATION=45, PATTERN_SPACING=6, PATTERN_THICK=3, $
  FILL_COLOR='green', XTITLE='Month', YTITLE='Value', $
  TITLE='Monthly Record', FONT_SIZE=12, MARGIN=0.1, /CURRENT)
IF fig_sav THEN win1.Save, 'figures/ng_barplot_1A.png', WIDTH=800

win2 = WINDOW(DIMENSIONS=[800, 600], /NO_TOOLBAR)
bpd1 = BARPLOT(months, data1, NBARS=2, INDEX=0, NAME='Data 1', $
  ;PATTERN_ORIENTATION=45, PATTERN_SPACING=6, PATTERN_THICK=3, $
  FILL_COLOR='green', XTICKINTERVAL=1, XMINOR=0, YRANGE=[0, 20], $
  XTITLE='Month', YTITLE='Value', TITLE='Monthly Record', $
  FONT_SIZE=12, MARGIN=0.1, /CURRENT)
bpd2 = BARPLOT(months, data2, NBARS=2, INDEX=1, NAME='Data 2', $
  ;PATTERN_ORIENTATION=45, PATTERN_SPACING=6, PATTERN_THICK=3, $
  FILL_COLOR='gold', /OVERPLOT)
lgd = LEGEND(TARGET=[bpd1, bpd2], POSITION=[10.6, 18.9], FONT_SIZE=12, /DATA)
IF fig_sav THEN win2.Save, 'figures/ng_barplot_1B.png', WIDTH=800

win3 = WINDOW(DIMENSIONS=[800, 600], /NO_TOOLBAR)
bpd1 = BARPLOT(months, data1, NAME='Data 1', $
  FILL_COLOR='green', XTICKINTERVAL=1, XMINOR=0, YRANGE=[0, 30], $
  ;PATTERN_ORIENTATION=45, PATTERN_SPACING=6, PATTERN_THICK=3, $
  XTITLE='Month', YTITLE='Value', TITLE='Monthly Record', $
  FONT_SIZE=12, MARGIN=0.1, /CURRENT)
bpd2 = BARPLOT(months, data1+data2, BOTTOM_VALUES=data1, NAME='Data 2', $
  ;PATTERN_ORIENTATION=45, PATTERN_SPACING=6, PATTERN_THICK=3, $
  FILL_COLOR='gold', /OVERPLOT)
lgd = LEGEND(TARGET=[bpd1, bpd2], POSITION=[10.6, 28.5], FONT_SIZE=12, /DATA)
IF fig_sav THEN win3.Save, 'figures/ng_barplot_1C.png', WIDTH=800

END