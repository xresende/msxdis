
          ; MSX BIOS
          ; ========
          ; 
          ; . Symbol table by MSX.BIOS by ASCII Corp., 1983 (v3.44)
          ; 
          ;     file       : BIOHDR.MAC
          ;     use        : Restart calls and ROM entries table
          ;     written by : Jey Suzuki, Rick Yamashita
          ;                  ASCII Corporation, Japan
          ; 
          ;     edit       : January, 1985
          ;     reason     : Zilog Z80 Mneumonic version and cleanup
          ;     edited by  : Steven M. Ting
          ; 
          ; . Disassembled by Ximenes R. Resende (xresende@gmail.com)
          ;     file       : EXPERT10.ROM
          ; 


BEGIN:                         ; MSX System Init

0x0000    di                   ; Fail safe
0x0001    jp   CHKRAM          ; Find all connected RAM
0x0004    dw   CGTABL          ; Address of character generator table to allow use of other character ROM

          ; ** VDP Information **
          ; Any program that access the VDP hardware directly
          ; should read the I/O port address found here, to be certain
          ; the software is compatible with future versions of the VDP

0x0006    db   98h             ; Port address for VDP data read
0x0007    db   98h             ; Port address for VDP data write

_SYNCHR:

0x0008    jp   SYNCHR
0x000B    db   00h

_RDSLT:

0x000C    jp   RDSLT
0x000F    db   00h

_CHRGTR:

0x0010    jp   CHRGTR
0x0013    db   00h

_WRSLT:

0x0014    jp   WRSLT
0x0017    db   00h

_OUTDO:

0x0018    jp   OUTDO           ; Output a char to the console or printer
0x001B    db   00h

_CALSLT:

0x001C    jp   CALSLT
0x001F    db   00h

_DCOMPR:

0x0020    jp   DCOMPR
0x0023    db   00h

_ENASLT:

0x0024    jp   ENASLT
0x0027    db   00h

_GETYPR:

0x0028    jp   GETYPR
0x002B    db   11h
0x002C    db   11h
0x002D    db   00h
0x002E    db   00h
0x002F    db   00h

_CALLF:

0x0030    jp   CALLF
0x0033    db   00h
0x0034    db   00h
0x0035    db   00h
0x0036    db   00h
0x0037    db   00h

          ; 
          ; Following are used for I/O initializations
          ; 

0x0038    jp   KEYINT          ; Handlers for hardware interrupt
0x003B    jp   INITIO          ; Device initialization
0x003E    jp   INIFNK          ; Reset all function key's text

          ; 
          ; The following entry points provide control of the 
          ; VDP's registers, screen mode settings, and memory block
          ; move between DRAM and VRAM.

0x0041    jp   DISSCR          ; Disable screen display
0x0044    jp   ENASCR          ; Enable screen display
0x0047    jp   ENASCR          ; Write a byte to any VDP register
0x004A    jp   RDVRM           ; Read VRAM address using [HL]
0x004D    jp   WRTVRM          ; Write VRAM address using [HL]
0x0050    jp   SETRD           ; Set up VDP for read
0x0053    jp   SETWRT          ; Set up VDP for write
0x0056    jp   FILVRM          ; Fill VRAM with specified data
0x0059    jp   LDIRMV          ; Move block of data from VRAM to memory
0x005C    jp   LDIRVM          ; Move block of data from memory to VRAM
0x005F    jp   CHGMOD          ; Change screen mode of VDP to [SCRMOD]
0x0062    jp   CHGCLR          ; Change fg, bg and border colors
0x0065    db   00h
0x0066    jp   NMI             ; Handler of non-maskarable interrupt
0x0069    jp   CLRSPR          ; Init sprite data
0x006C    jp   INITXT          ; Init VDP for 40 x 24 text mode (SCREEN 0)
0x006F    jp   INIT32          ; Init VDP for 32 x 24 text mode (SCREEN 1)
0x0072    jp   INIGRP          ; Init VDP for high resolution mode (SCREEN 2)
0x0075    jp   INIMLT          ; Init VDP for multi color mode (SCREEN 3)
0x0078    jp   SETTXT          ; Set VDP display 40 x 24 text mode
0x007B    jp   SETT32          ; Set VDP display 32 x 24 text mode
0x007E    jp   SETGRO          ; Set VDP display high resolution mode
0x0081    jp   SETMLT          ; Set VDP display multi color mode
0x0084    jp   CALPAT          ; Get address of sprite pattern table
0x0087    jp   CALATR          ; Get address of sprite attribute table
0x008A    jp   GSPSIZ          ; Return current sprite size
0x008D    jp   GRPPRT          ; Print a char on the graphic screen

          ; 
          ; The following entry points are used for PSG initialization, 
          ; read and write PSG registers, and PLAY statement execution.

0x0090    jp   GICINI          ; Init PSG and static data for PLAY
0x0093    jp   WRTPSG          ; Write data to PSG
0x0096    jp   RDPSG           ; Read data from PSG
0x0099    jp   STRTMS          ; Check and start bg task for PLAY

          ; 
          ; General INPUT and PRINT utilities.
          ; 

0x009C    jp   CHSNS           ; Check keyboard status
0x009F    jp   CHGET           ; Return char typed, with wait
0x00A2    jp   CHPUT           ; Output character to console
0x00A5    jp   LPTOUT          ; Output character to printer, if possible
0x00A8    jp   LPTSTT          ; Check status of line printer
0x00AB    jp   CNVCHR          ; Check for graphic header byte and convert code
0x00AE    jp   PINLIN          ; Read line from keyboard to buffer
0x00B1    jp   INLIN           ; Same as above, except in case of AUTFLG is set
0x00B4    jp   QINLIN          ; Print a "?", then jump to INLIN
0x00B7    jp   BREAKX          ; [CTRL+STOP] pressed?
0x00BA    jp   ISCNTC          ; [SHIFT+STOP] pressed?
0x00BD    jp   CKCNTC          ; Same as ISCNTC, but used by BASIC
0x00C0    jp   BEEP            ; Buzz
0x00C3    jp   CLS             ; Clear screen
0x00C6    jp   POSIT           ; Place cursor at column [H], row [L]
0x00C9    jp   FNKSB           ; Display function keys, if necessary
0x00CC    jp   ERAFNK          ; Stop displaying the function keys
0x00CF    jp   DSPFNK          ; Enable funcion keys display
0x00D2    jp   TOTEXT          ; Force screen to text mode

          ; 
          ; General INPUT and PRINT utilities.
          ; 

0x00D5    jp   GTSTCK          ; 
0x00D8    jp   GTTRIG          ; 
0x00DB    jp   GTPAD           ; 
0x00DE    jp   GTPDL           ; 

          ; 
          ; Following are used to access the cassette tape, 
          ; data read/write, and motor on/off
          ; 

0x00E1    jp   TAPION          ; 
0x00E4    jp   TAPIN           ; 
0x00E7    jp   TAPIOF          ; 
0x00EA    jp   TAPOON          ; 
0x00ED    jp   TAPOUT          ; 
0x00F0    jp   TAPOFF          ; 
0x00F3    jp   STMOTR          ; 

          ; 
          ; BASIC queues
          ; 

0x00F6    jp   LFTQ            ; 
0x00F9    jp   PUTQ            ; 

          ; 
          ; For BASIC interpreter's GENGRP and ADVGRP modules use
          ; 

0x00FC    jp   0x16C5
0x00FF    jp   0x16EE
0x0102    jp   0x175D
0x0105    jp   0x173C
0x0108    jp   0x172A
0x010B    jp   0x170A
0x010E    jp   0x1599
0x0111    jp   0x15DF
0x0114    jp   0x1639
0x0117    jp   0x1640
0x011A    jp   0x1676
0x011D    jp   0x1647
0x0120    jp   0x167E
0x0123    jp   0x1809
0x0126    jp   0x18C7
0x0129    jp   0x18CF
0x012C    jp   0x18E4
0x012F    jp   0x197A
0x0132    jp   0x0F3D
0x0135    jp   0x0F7A
0x0138    jp   0x144C
0x013B    jp   0x144F
0x013E    jp   0x1449
0x0141    jp   0x1452
0x0144    jp   0x148A
0x0147    jp   0x148E
0x014A    jp   0x145F
0x014D    jp   0x1B63
0x0150    jp   0x1470
0x0153    jp   0x1474
0x0156    jp   0x0468
0x0159    jp   CALBAS
0x015C    db   C3h             ; RESERVED FOR EXPANSION - start
0x015D    db   B6h
0x015E    db   01h
0x015F    db   4Bh
0x0160    db   02h
0x0161    db   28h
0x0162    db   43h
0x0163    db   54h
0x0164    db   4Bh
0x0165    db   50h
0x0166    db   43h
0x0167    db   02h
0x0168    db   2Fh
0x0169    db   43h
0x016A    db   45h
0x016B    db   47h
0x016C    db   46h
0x016D    db   51h
0x016E    db   02h
0x016F    db   2Ah
0x0170    db   4Bh
0x0171    db   56h
0x0172    db   51h
0x0173    db   50h
0x0174    db   51h
0x0175    db   54h
0x0176    db   4Bh
0x0177    db   02h
0x0178    db   35h
0x0179    db   52h
0x017A    db   47h
0x017B    db   54h
0x017C    db   43h
0x017D    db   50h
0x017E    db   46h
0x017F    db   47h
0x0180    db   4Eh
0x0181    db   4Eh
0x0182    db   4Bh
0x0183    db   02h
0x0184    db   30h
0x0185    db   47h
0x0186    db   49h
0x0187    db   54h
0x0188    db   47h
0x0189    db   4Bh
0x018A    db   54h
0x018B    db   51h
0x018C    db   55h
0x018D    db   02h
0x018E    db   28h
0x018F    db   4Bh
0x0190    db   54h
0x0191    db   4Fh
0x0192    db   4Bh
0x0193    db   50h
0x0194    db   51h
0x0195    db   02h
0x0196    db   35h
0x0197    db   4Bh
0x0198    db   45h
0x0199    db   51h
0x019A    db   50h
0x019B    db   4Bh
0x019C    db   02h
0x019D    db   23h
0x019E    db   58h
0x019F    db   4Bh
0x01A0    db   4Eh
0x01A1    db   43h
0x01A2    db   02h
0x01A3    db   36h
0x01A4    db   51h
0x01A5    db   5Ch
0x01A6    db   5Ch
0x01A7    db   4Bh
0x01A8    db   02h
0x01A9    db   25h
0x01AA    db   54h
0x01AB    db   57h
0x01AC    db   5Ch
0x01AD    db   02h
0x01AE    db   FFh
0x01AF    db   FFh
0x01B0    db   FFh
0x01B1    db   FFh
0x01B2    db   FFh
0x01B3    db   FFh
0x01B4    db   FFh
0x01B5    db   FFh             ; RESERVED FOR EXPANSION - end

          ; 
          ; SLOTS
          ; 
          ; Every cartridge located at 0000-3FFFH must contain codes in
          ; this module which are entered via following addresses.
          ; 
          ;    0x000C RDSLT
          ;    0x0014 WRSLT
          ;    0x001C CALSLT
          ;    0x0024 ENASLT
          ; 
          ; ===== RDSLT =====
          ; 
          ; Select the appropriate slot according to the value given
          ; through registers, and read the content of memory from the
          ; slot.
          ; 
          ; Input parameters:
          ; 
          ;   A - FxxxSSPP
          ;       |   ||||
          ;       |   ||++-- primary slot # (0-3)
          ;       |   ++---- secondary slot # (0-3)
          ;       +--------- 1 if secondary slot # specified
          ; 
          ;   HL - address of target memory
          ; 
          ; Returned value
          ; 
          ;   A - content of memory
          ; 
          ; Note: Interrupts are disabled automatically but never enabled
          ;       by this routine.
          ; 


RDSLT:

0x01B6    call SELPRM
0x01B9    jp   m,RDESLT
0x01BC    in   a,(A8h)
0x01BE    ld   d,a
0x01BF    and  c
0x01C0    or   b
0x01C1    call RAMLOW
0x01C4    ld   a,e
0x01C5    ret

RDESLT:

0x01C6    push hl
0x01C7    call SELEXP
0x01CA    ex   (sp),hl
0x01CB    push bc
0x01CC    call RDSLT
0x01CF    jr   WRESED

WRSLT:

0x01D1    push de
0x01D2    call SELPRM
0x01D5    jp   m,WRESLT
0x01D8    pop  de
0x01D9    in   a,(A8h)
0x01DB    ld   d,a
0x01DC    and  c
0x01DD    or   b
0x01DE    jp   WRPRIM

WRESLT:

0x01E1    ex   (sp),hl
0x01E2    push hl
0x01E3    call SELEXP
0x01E6    pop  de
0x01E7    ex   (sp),hl
0x01E8    push bc
0x01E9    call WRSLT

WRESED:

0x01EC    pop  bc
0x01ED    ex   (sp),hl
0x01EE    push af
0x01EF    ld   a,b
0x01F0    and  3Fh
0x01F2    or   c
0x01F3    out  (A8h),a
0x01F5    ld   a,l
0x01F6    ld   (0xFFFF),a
0x01F9    ld   a,b
0x01FA    out  (A8h),a
0x01FC    pop  af
0x01FD    pop  hl
0x01FE    ret

CALBAS:

0x01FF    ld   iy,(0xFCC0)
0x0203    jr   CALSLT

CALLF:

0x0205    ex   (sp),hl
0x0206    push af
0x0207    push de
0x0208    ld   a,(hl)
0x0209    push af
0x020A    pop  iy
0x020C    inc  hl
0x020D    ld   e,(hl)
0x020E    inc  hl
0x020F    ld   d,(hl)
0x0210    inc  hl
0x0211    push de
0x0212    pop  ix
0x0214    pop  de
0x0215    pop  af
0x0216    ex   (sp),hl

CALSLT:

0x0217    exx
0x0218    ex   af,af'
0x0219    push iy
0x021B    pop  af
0x021C    push ix
0x021E    pop  hl
0x021F    call SELPRM
0x0222    jp   m,CALESL
0x0225    in   a,(A8h)
0x0227    push af
0x0228    and  c
0x0229    or   b
0x022A    exx
0x022B    jp   CLPRIM

CALESL:

0x022E    call SELEXP
0x0231    push af
0x0232    pop  iy
0x0234    push hl
0x0235    push bc
0x0236    ld   c,a
0x0237    ld   b,0
0x0239    ld   a,l
0x023A    and  h
0x023B    or   d
0x023C    ld   hl,SLTTBL       ; Cópia dos registradores de slot primário
0x023F    add  hl,bc
0x0240    ld   (hl),a
0x0241    push hl
0x0242    ex   af,af'
0x0243    exx
0x0244    call CALSLT
0x0247    exx
0x0248    ex   af,af'
0x0249    pop  hl
0x024A    pop  bc
0x024B    pop  de
0x024C    ld   a,b
0x024D    and  3Fh
0x024F    or   c
0x0250    di
0x0251    out  (A8h),a
0x0253    ld   a,e
0x0254    ld   (0xFFFF),a
0x0257    ld   a,b
0x0258    out  (A8h),a
0x025A    ld   (hl),e
0x025B    ex   af,af'
0x025C    exx
0x025D    ret

ENASLT:

0x025E    call SELPRM
0x0261    jp   m,ENESLT
0x0264    in   a,(A8h)
0x0266    and  c
0x0267    or   b
0x0268    out  (A8h),a
0x026A    ret

ENESLT:

0x026B    push hl
0x026C    call SELEXP
0x026F    ld   c,a
0x0270    ld   b,0
0x0272    ld   a,l
0x0273    and  h
0x0274    or   d
0x0275    ld   hl,SLTTBL       ; Cópia dos registradores de slot primário
0x0278    add  hl,bc
0x0279    ld   (hl),a
0x027A    pop  hl
0x027B    ld   a,c
0x027C    jr   ENASLT

SELPRM:

0x027E    di
0x027F    push af
0x0280    ld   a,h
0x0281    rlca
0x0282    rlca
0x0283    and  03h
0x0285    ld   e,a
0x0286    ld   a,-64

SLPRM1:

0x0288    rlca
0x0289    rlca
0x028A    dec  e
0x028B    jp   p,SLPRM1
0x028E    ld   e,a
0x028F    cpl
0x0290    ld   c,a
0x0291    pop  af
0x0292    push af
0x0293    and  03h
0x0295    inc  a
0x0296    ld   b,a
0x0297    ld   a,-85

SLPRM2:

0x0299    add  a,85
0x029B    djnz SLPRM2
0x029D    ld   d,a
0x029E    and  e
0x029F    ld   b,a
0x02A0    pop  af
0x02A1    and  a
0x02A2    ret

SELEXP:

0x02A3    push af
0x02A4    ld   a,d
0x02A5    and  C0h
0x02A7    ld   c,a
0x02A8    pop  af
0x02A9    push af
0x02AA    ld   d,a
0x02AB    in   a,(A8h)
0x02AD    ld   b,a
0x02AE    and  3Fh
0x02B0    or   c
0x02B1    out  (A8h),a
0x02B3    ld   a,d
0x02B4    rrca
0x02B5    rrca
0x02B6    and  03h
0x02B8    ld   d,a
0x02B9    ld   a,-85

SLEXP1:

0x02BB    add  a,85
0x02BD    dec  d
0x02BE    jp   p,SLEXP1
0x02C1    and  e
0x02C2    ld   d,a
0x02C3    ld   a,e
0x02C4    cpl
0x02C5    ld   h,a
0x02C6    ld   a,(0xFFFF)
0x02C9    cpl
0x02CA    ld   l,a
0x02CB    and  h
0x02CC    or   d
0x02CD    ld   (0xFFFF),a
0x02D0    ld   a,b
0x02D1    out  (A8h),a
0x02D3    pop  af
0x02D4    and  03h
0x02D6    ret
