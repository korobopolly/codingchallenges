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

    # 3. 각 article 노드에 대해 멤버 계산
    result = []
    for entry in article:
        nodes = entry.split()
        notified_members = set()

        # 각 노드별로 조상 포함 멤버 계산
        for node in nodes:
            all_categories = get_ancestors(parent_map, node)
            all_categories.add(node)  # 자기 자신도 포함 (집합에 추가)

            # 해당 카테고리에 속한 멤버 추가
            for cat in all_categories:
                if cat in category_to_members:
                    notified_members.update(category_to_members[cat])

        # 알림받는 멤버 수 추가
        result.append(len(notified_members))

    return result

print(solution(["culture","music","movie","pop","jazz","economy","technology","health","ai"],
               ["culture music","culture movie", "music pop", "music jazz", "technology health", "technology ai"],
               ["Covy culture economy","Teo music pop jazz","Felix health ai pop jazz"],
               ["economy","pop","ai technology movie"]))