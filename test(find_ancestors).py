def build_parent_map(relations):
    parent_map = {}  # 자식 -> 부모 관계 저장 #딕셔너리(키로 검색하기 위함)
    for relation in relations:
        parent, child = relation.split()  # 관계를 부모와 자식으로 나눔
        parent_map[child] = parent
    #parent_map {'music': 'culture', 'movie': 'culture', 'pop': 'music', 'jazz': 'music', 'health': 'technology', 'ai': 'technology'}
    return parent_map

def get_ancestors(parent_map, node):
    ancestors = set()  # 집합으로 초기화
    while node in parent_map:  # 부모가 있는 동안 반복
        parent = parent_map[node]
        ancestors.add(parent)
        node = parent  # 부모로 이동
    # set()
    # {'culture', 'music'}
    # {'technology'}
    # set()
    # {'culture'}
    return ancestors

def solution(category, relation, member, article):
    # 1. 부모-자식 관계 맵 생성
    parent_map = build_parent_map(relation)

    # 2. 멤버 -> 카테고리 매핑
    category_to_members = {}
    for m in member:
        parts = m.split()
        mem_name = parts[0]  # 멤버 이름
        for cat_name in parts[1:]:  # 멤버가 속한 모든 카테고리
            if cat_name not in category_to_members:
                category_to_members[cat_name] = set()
            category_to_members[cat_name].add(mem_name)
    # {'culture': {'Covy'}, 'economy': {'Covy'}, 'music': {'Teo'}, 'pop': {'Felix', 'Teo'}, 'jazz': {'Felix', 'Teo'}, 'health': {'Felix'}, 'ai': {'Felix'}}

    # 3. 각 article 노드에 대해 멤버 계산
    result = {}
    for entry in article:
        nodes = entry.split()
        notified_members = set()
        # ['economy']
        # ['pop']
        # ['ai', 'technology', 'movie']

        # 각 노드별로 조상 포함 멤버 계산
        for node in nodes:
            all_categories = get_ancestors(parent_map, node)
            all_categories.add(node)  # 자기 자신도 포함
            # 1.
            # {'economy'}
            # 2.
            # {'music', 'pop', 'culture'}
            # 3.
            # {'technology', 'ai'}
            # {'technology'}
            # {'movie', 'culture'}

            # 해당 카테고리에 속한 멤버 추가
            for cat in all_categories:
                if cat in category_to_members:
                    notified_members.update(category_to_members[cat])

        # 현재 entry에 대한 알림 멤버 수
        result[entry] = len(notified_members)

    return result


print(solution(["culture","music","movie","pop","jazz","economy","technology","health","ai"],
               ["culture music","culture movie", "music pop", "music jazz", "technology health", "technology ai"],
               ["Covy culture economy","Teo music pop jazz","Felix health ai pop jazz"],
               ["economy","pop","ai technology movie"]))