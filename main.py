# 파일이름 : 사이버 펑크, 픽셀 카페 레시피 수사국!
# 작 성 자 : 60232229 조재휴

agent_name = ""       
security_level = 0    
bean_weight = 0.0     
recipe_list = []      
total_coffee = 0      

print(f"--- [픽셀 카페 레시피 수사국 시스템 접속] ---")

agent_name = str(input("요원 코드네임을 입력하십시오: "))

print(f"\n[{agent_name} 요원 보안 자격 심사를 시작합니다]")
mission_score = int(input("- 임무 수행 횟수를 입력하십시오 (0~100): "))
success_rate = float(input("- 데이터 복원 성공률을 입력하십시오 (0.0~1.0): "))
years_active = int(input("- 요원 활동 경력을 입력하십시오 (년 단위): "))


# 공식: (미션점수 * 0.4) + (성공률 * 100 * 0.5) + (요원 활동 경력 * 10)
final_score = (mission_score * 0.4) + (success_rate * 100 * 0.5) + (years_active * 10)

if final_score >= 80:
    security_level = 5
    rank_name = "S급 시니어 요원"
elif final_score >= 50:
    security_level = 3
    rank_name = "A급 정예요원"
else:
    security_level = 1
    rank_name = "C급 신입 요원"

print(f"\n[심사 완료] 최종 점수 {final_score:.1f}점으로 {rank_name}(등급 {security_level})에 임명되었습니다.")



bean_weight = float(input(f"\n분석할 원두의 무게(g)를 입력하십시오: "))


print(f"\n--- 임무: {rank_name} 권한으로 레시피 데이터 3개를 복원하십시오 ---")
for i in range(3):
    water = int(input(f"{i+1}번째 데이터(물의 양 ml) 입력: "))
    recipe_list.append(water)

recipe_count = len(recipe_list)
recipe_total = sum(recipe_list)
recipe_list.sort()

print(f"\n분석 결과: 총 {recipe_count}개 데이터 수집, 총량 {recipe_total}ml.")
print(f"정렬된 수치: {recipe_list}")


print(f"\n--- 시스템 최종 판정 ---")
if security_level >= 3:
    if recipe_total >= 500:
        print("결과: [고급 레시피 복원 성공] 인류의 기억이 1% 회복되었습니다.")
      
        if recipe_list[-1] > 300:
            print("경고: 단일 추출량이 기준치를 초과했습니다. 농도를 조절하십시오.")
    else:
        print("결과: [데이터 부족] 고급 요원 권한은 있으나, 추출량이 기준치 미만입니다.")


else:
    if security_level < 3 or recipe_total < 500:
        print("결과: [일반 레시피 복원 완료] 시스템 출력이 제한적입니다.")
    else:
        print("결과: [데이터 불일치] 재분석이 필요합니다.")

total_coffee += recipe_total
print(f"\n최종 누적 제조량: {total_coffee}ml")
print(f"--- {agent_name} 요원, 시스템을 종료합니다. ---")
