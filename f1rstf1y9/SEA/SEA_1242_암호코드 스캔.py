decode = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
          '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

# decode 딕셔너리 활용하여 이진수 코드를 십진수 코드로 변환, 만약 decode에 없다면 0 반환
def get_code(tmp):
    code = []
    for i in range(8):
        c = decode.get(tmp[i*7:i*7+7])
        if c is None:
            return 0
        code.append(c)
    return code

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    lst = set()

    # 입력받는 줄마다 양옆의 0을 제거하여 중복없이 리스트에 저장
    for _ in range(N):
        tmp = input().strip().strip('0')
        if tmp:
            lst.add(tmp)

    codes = set()
    for l in lst:
        # 리스트에 저장된 줄을 이진수로 변환하고 이진수 코드의 맨오른쪽은 무조건 1이므로 rstrip('0')
        tmp = bin(int(l,16)).lstrip('0b').rstrip('0')

        # 비율을 1로 시작 (1이면 길이 56, 2면 길이 112...)
        i = 1
        while tmp:
            # 길이보다 모자란 0 채우기
            tmp = tmp.zfill(56*i)
            # 길이만큼 이진수 코드 잘라서 유효한 코드 얻어낼 수 있는지 확인
            code = get_code(tmp[-56*i::i])
            if code: # 십진수 코드 얻었으면
                codes.add(tuple(code)) # code set에 저장
                tmp = tmp[:len(tmp)-56*i].rstrip('0') # 오른쪽 0제거하고 해당 줄에서 찾은 부분 제거
                i = 0 # 비율 초기화
            # 현재 비율에서 유효한 코드 못 얻어냈다면 비율 1 증가
            i += 1

    # 얻어낸 코드 각각 정상코드인지 확인 - "(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드"가 10의 배수
    ans = 0
    for code in codes:
        tmp = 0
        for i in range(8):
            tmp += code[i] * (1 if i%2 else 3)
        # 정상 코드라면 ans 변수에 코드에 포함된 숫자 합 더하기
        if not tmp%10:
            ans += sum(code)

    print(f"#{t+1} {ans}")