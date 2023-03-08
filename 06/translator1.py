entire_code = []
with open("RectL.asm","r") as f:      # 파일 읽기
    while True:
        line=f.readline()
        if not line:                # 파일의 끝 확인
            break 
        line = line.strip()       # 앞 뒤 공백 제거
        if line.startswith('//') or len(line) == 0: # 주석 또는 빈 문자열 제거
            continue

        print(line)          # line 출력

        if line.startswith('@'):    # A 코드 처리
            code = '0'
            code += bin(int(line[1:]))[2:].rjust(15,'0') 
        else :                      # B 코드 처리
            # C code 111accccccdddjjj :
            # a : 계산시 A대신 M
            # c : ALU에 넣을 계산의 방법
            # d : dest 각각 ADM
            # j : jump 각각 < = >
            code = list('1110cccccc000000')
            line = line.split('=',maxsplit=2)
            if len(line) == 1:
                line.insert(0,'')
            line[1] = line[1].split(';',maxsplit=2)       # 코드 =과 ;로 나누기
            line[1].append('')

            if('A' in line[0]):                                         # dest 처리
                code[10] = '1'
            if('D' in line[0]):
                code[11] = '1'
            if('M' in line[0]):
                code[12] = '1'

            jump_mark = ['','JGT','JEQ','JGE','JLT','JNE','JLE','JMP']  # jump 처리
            for i in range(len(jump_mark)) :
                if line[1][1].strip('') == jump_mark[i] :
                    code[13:] = bin(i)[2:].rjust(3,'0')


            comp_table = [[                                             # comp 처리
                    '0', '1', '-1', 'D', 'A', '!D', '!A', '-D', '-A', 'D+1', 'A+1', 'D-1',
                    'A-1', 'D+A', 'D-A', 'A-D', 'D&A', 'D|A'
                ],[
                    '101010','111111','111010','001100','110000','001101','110001',
                   '001111','110011','011111','110111','001110','110010','000010','010011',
                   '000111','000000','010101'
                ]
            ]
            if 'M' in line[1][0] :
                code[3] = '1'
                line[1][0] = line[1][0].replace('M', 'A')

            for i in range(len(comp_table[0])) :
                if line[1][0].strip('') == comp_table[0][i] :
                    code[4:10] = list(comp_table[1][i])

            code = ''.join(code)

        print(code)
        entire_code.append(code)
print()
with open("RectL.hack","w") as f:
    for i in entire_code:
        print(i)
        f.write(i + '\n')
