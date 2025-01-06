# 카멜케이스를 쓰는 경우는 클래스의 이름에 사용하고 나머지는 스네이크 쓰면 될 듯
def get_example(file_name):
    with open(file_name, 'r') as file:
        example_count = 0
        examples = {}
        # print(file, '1')
        for line in file:
            example_count += 1
            examples[f"example{example_count}"] = line.strip() # 개형문자열에 의해서 strip()을 해줘야지 안하면 공백이 생김
    return examples

"""
with open(file_name, 'r') as file:
        example_count = len(file.readlines())
        example = {}
        # print(file, '1')
        for line in file:
            print(line.strip())
이렇게 작성하면 읽는 포인턱 example_count에서 가장 아래에 위치하기에 for반복문이 읽을거리가 없어짐
그래서 수정을 위와 같이 했음
"""