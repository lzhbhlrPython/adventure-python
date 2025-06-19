import enum
import random
import typing as Ty
import matplotlib.pyplot as plt
import tqdm

class GeneEnum(enum.Enum):
    pass

class BloodTypeEnum(enum.Enum):
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"


class ABOGeneEnum(GeneEnum):
    A_PURE = "AA"
    A_MIXED_1 = "AO"
    A_MIXED_2 = "OA"
    B_PURE = "BB"
    B_MIXED_1 = "BO"
    B_MIXED_2 = "OB"
    O_PURE = "OO"
    AB_1 = "AB"
    AB_2 = "BA"
    O = "OO"

class RhFactorEnum(GeneEnum):
    POSITIVE_PURE = "RR"
    POSITIVE_MIXED_1 = "Rr"
    POSITIVE_MIXED_2 = "rR"
    NEGATIVE = "rr"

def blood_test(abo: str, rh: str) -> Ty.Optional[BloodTypeEnum]:
    if rh == RhFactorEnum.POSITIVE_PURE.value or rh == RhFactorEnum.POSITIVE_MIXED_1.value or rh == RhFactorEnum.POSITIVE_MIXED_2.value:
        if abo == ABOGeneEnum.A_PURE.value or abo == ABOGeneEnum.A_MIXED_1.value or abo == ABOGeneEnum.A_MIXED_2.value:
            return BloodTypeEnum.A_POSITIVE
        elif abo == ABOGeneEnum.B_PURE.value or abo == ABOGeneEnum.B_MIXED_1.value or abo == ABOGeneEnum.B_MIXED_2.value:
            return BloodTypeEnum.B_POSITIVE
        elif abo == ABOGeneEnum.AB_1.value or abo == ABOGeneEnum.AB_2.value:
           return BloodTypeEnum.AB_POSITIVE
        elif abo == ABOGeneEnum.O_PURE.value or abo == ABOGeneEnum.O.value:
            return BloodTypeEnum.O_POSITIVE
        else:
            print(f"Invalid ABO gene: {abo}")
            raise ValueError("Invalid ABO gene for positive Rh factor")
    elif rh == RhFactorEnum.NEGATIVE.value:
        if abo == ABOGeneEnum.A_PURE.value or abo == ABOGeneEnum.A_MIXED_1.value or abo == ABOGeneEnum.A_MIXED_2.value:
            return BloodTypeEnum.A_NEGATIVE
        elif abo == ABOGeneEnum.B_PURE.value or abo == ABOGeneEnum.B_MIXED_1.value or abo == ABOGeneEnum.B_MIXED_2.value:
            return BloodTypeEnum.B_NEGATIVE
        elif abo == ABOGeneEnum.AB_1.value or abo == ABOGeneEnum.AB_2.value:
            return BloodTypeEnum.AB_NEGATIVE
        elif abo == ABOGeneEnum.O_PURE.value or abo == ABOGeneEnum.O.value:
            return BloodTypeEnum.O_NEGATIVE
        else:
            print(f"Invalid ABO gene: {abo}")
            raise ValueError("Invalid ABO gene for negative Rh factor")
    else:
        print(f"Invalid Rh factor: {rh}")
        raise ValueError("Invalid Rh factor")
def gene_string2_gene_enum(gene_str: str) -> Ty.Optional[GeneEnum]:
    if gene_str=="AA":
        return ABOGeneEnum.A_PURE
    elif gene_str=="BB":
        return ABOGeneEnum.B_PURE
    elif gene_str=="OO":
        return ABOGeneEnum.O_PURE
    elif gene_str=="AB":
        return ABOGeneEnum.AB_1
    elif gene_str=="BA":
        return ABOGeneEnum.AB_2
    elif gene_str=="AO":
        return ABOGeneEnum.A_MIXED_1
    elif gene_str=="OA":
        return ABOGeneEnum.A_MIXED_2
    elif gene_str=="BO":
        return ABOGeneEnum.B_MIXED_1
    elif gene_str=="OB":
        return ABOGeneEnum.B_MIXED_2
    elif gene_str=="RR":
        return RhFactorEnum.POSITIVE_PURE
    elif gene_str=="Rr":
        return RhFactorEnum.POSITIVE_MIXED_1
    elif gene_str=="rR":
        return RhFactorEnum.POSITIVE_MIXED_2
    elif gene_str=="rr":
        return RhFactorEnum.NEGATIVE
    

class Blood:
    def __init__(self, abo_gene: GeneEnum, rh_factor: GeneEnum):
        if not isinstance(abo_gene, GeneEnum):
            raise ValueError("ABO gene must be an instance of GeneEnum")
        if not isinstance(rh_factor, GeneEnum):
            raise ValueError("Rh factor must be an instance of GeneEnum")
        if abo_gene not in ABOGeneEnum:
            raise ValueError("Invalid ABO gene")
        if rh_factor not in RhFactorEnum:
            raise ValueError("Invalid Rh factor")
        self.abo_gene = abo_gene
        self.rh_factor = rh_factor
        self.blood_type = self._determine_blood_type()
    def _determine_blood_type(self) -> BloodTypeEnum:
        abo=self.abo_gene.value
        rh = self.rh_factor.value
        blood_test_result = blood_test(abo, rh)
        if blood_test_result is None:
            raise ValueError("Invalid ABO gene or Rh factor")
        return blood_test_result
    
    def __str__(self):
        return f"{self.blood_type.value} ({self.abo_gene.value}, {self.rh_factor.value})"

    def __add__(self, other):
        if not isinstance(other, Blood):
            raise ValueError("Can only add another Blood instance")
        # Randomly choose one gene from each blood type
        new_ABO_pwd1 = random.choice(self.abo_gene.value)
        new_ABO_pwd2 = random.choice(other.abo_gene.value)
        new_ABO_gene = ABOGeneEnum(new_ABO_pwd1 + new_ABO_pwd2)

        new_RH_pwd1 = random.choice(self.rh_factor.value)
        new_RH_pwd2 = random.choice(other.rh_factor.value)
        new_rh_factor = RhFactorEnum(new_RH_pwd1 + new_RH_pwd2)
        # Create a new Blood instance with the combined genes

        return Blood(new_ABO_gene, new_rh_factor)

        

# 人群中的广泛性实验
class CrowdStudy:
    def __init__(self, population_size: int):
        self.population_size = population_size
        self.population = self._generate_population()

    def _generate_population(self) -> Ty.List[Blood]:
        #基因密码子平均分配
        population = []
        for i in tqdm.tqdm(range(self.population_size),colour='#99ff99',desc='生成人群'):
            # 生成随机的ABO和Rh因子
            ABO_gene=random.choice("ABO")+random.choice("ABO")
            rh_factor = random.choice("Rr") + random.choice("Rr")
            # 创建Blood实例
            abo_gene_enum = gene_string2_gene_enum(ABO_gene)
            rh_factor_enum = gene_string2_gene_enum(rh_factor)
            if abo_gene_enum is None or rh_factor_enum is None:
                raise ValueError(f"Invalid gene string: ABO={ABO_gene}, Rh={rh_factor}")
            blood = Blood(abo_gene_enum, rh_factor_enum)
            population.append(blood)
        return population
    def add_blood(self, blood: Blood):
        if not isinstance(blood, Blood):
            raise ValueError("Can only add a Blood instance")
        self.population.append(blood)
    def remove_blood(self, bloodIndex: int):
        if bloodIndex < 0 or bloodIndex >= len(self.population):
            raise IndexError("Blood index out of range")
        self.population.pop(bloodIndex)
    def clear_population(self):
        self.population.clear()
    
    def get_population_size(self) -> int:
        return len(self.population)
    def get_population(self) -> Ty.List[Blood]:
        return self.population
    
def analyze_population(crowd_study: CrowdStudy) -> Ty.Dict[str, Ty.Dict[str, Ty.Any]]:
    population = crowd_study.get_population()
    blood_type_counts = {}
    for blood in population:
        if blood.blood_type in blood_type_counts:
            blood_type_counts[blood.blood_type] += 1
        else:
            blood_type_counts[blood.blood_type] = 1

    data= {}
    for blood_type, count in blood_type_counts.items():
        print(f"Blood Type: {blood_type.value}")
        print(f"Count: {count}")
        print(f"Percentage: {count / len(population) * 100:.3f}%")
        data[blood_type.value] = {'count': count,
                                  'percentage': count / len(population) * 100,
                                  'blood_type': blood_type
                                  }
    
    return data
def main():
    initial_population_size = 10
    born_size = 1000000
    city_population = CrowdStudy(initial_population_size)
    """    
    city_population = CrowdStudy(0)
    for i in tqdm.tqdm(range(int(initial_population_size/2)), colour='#99ff99', desc='初始化人群A'):
        # 生成随机的ABO和Rh因子
        ABO_gene = "AO"
        Rh_gene = "Rr"
        # 创建Blood实例
        abo_gene_enum = gene_string2_gene_enum(ABO_gene)
        rh_factor_enum = gene_string2_gene_enum(Rh_gene)
        if abo_gene_enum is None or rh_factor_enum is None:
            raise ValueError(f"Invalid gene string: ABO={ABO_gene}, Rh={Rh_gene}")
        blood = Blood(abo_gene_enum, rh_factor_enum)
        city_population.add_blood(blood)
    for i in tqdm.tqdm(range(int(initial_population_size/2)), colour='#99ff99', desc='初始化人群B'):
        ABO_gene = "BO"
        Rh_gene = "Rr"
        # 创建Blood实例
        abo_gene_enum = gene_string2_gene_enum(ABO_gene)
        rh_factor_enum = gene_string2_gene_enum(Rh_gene)
        if abo_gene_enum is None or rh_factor_enum is None:
            raise ValueError(f"Invalid gene string: ABO={ABO_gene}, Rh={Rh_gene}")
        blood = Blood(abo_gene_enum, rh_factor_enum)
        city_population.add_blood(blood)
    """
    print("Initial Population:")
    print("Analyzing Population:")
    initial_data = analyze_population(city_population)
    for _ in tqdm.tqdm(range(born_size), colour='#ff9999', desc='模拟出生人口'):
        #city_population.add_blood(random.choice(city_population.get_population())+random.choice(city_population.get_population()))
        parent1 = random.randint(0, len(city_population.population) - 1)
        parent2 = random.randint(0, len(city_population.population) - 1)
        while parent1 == parent2:
            parent2 = random.randint(0, len(city_population.population) - 1)
        blood1 = city_population.population[parent1]
        blood2 = city_population.population[parent2]
        new_blood = blood1 + blood2
        city_population.add_blood(new_blood)
    print("\nPopulation After Adding New Blood Types:")
    for _ in tqdm.tqdm(range(initial_population_size), colour='#ff9999', desc='死亡初始人口'):
        city_population.population.pop(_)
    final_data=analyze_population(city_population)
    
    # 绘制两张饼图左右对比
    plt.style.use('ggplot')  # 使用ggplot样式
    blood_type_colors = {
        'A+': '#ff9999', 'A-': '#ff6666',
        'B+': '#66b3ff', 'B-': '#3399ff',
        'AB+': '#99ff99', 'AB-': '#66cc66',
        'O+': '#ffcc99', 'O-': '#ffaa66'
    }
    
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    labels1 = []
    data1 = []
    colors1 = []
    
    for key, value in tqdm.tqdm(initial_data.items(), colour='#66b3ff', desc='绘制初始人群血型饼图'):
        labels1.append('{blood_type} ({percentage})'.format(
            blood_type=value['blood_type'].value,
            percentage=f"{value['percentage']:.4f}%"
        ))
        data1.append(value['count'])
        colors1.append(blood_type_colors[value['blood_type'].value])
    
    plt.title('Initial Population Blood Types'+'\n'+'Population Size: ' + str(initial_population_size))
    plt.pie(data1, labels=labels1, autopct='%1.1f%%', startangle=140, colors=colors1)

    plt.subplot(1, 2, 2)
    labels2 = []
    data2 = []
    colors2 = []
    
    for key, value in tqdm.tqdm(final_data.items(), colour='#66b3ff', desc='绘制最终人群血型饼图'):
        labels2.append('{blood_type} ({percentage})'.format(
            blood_type=value['blood_type'].value,
            percentage=f"{value['percentage']:.4f}%"
        ))
        data2.append(value['count'])
        colors2.append(blood_type_colors[value['blood_type'].value])
    
    plt.title('Final Population Blood Types'+'\n'+'Population Size: ' + str(len(city_population.population)))
    plt.pie(data2, labels=labels2, autopct='%1.1f%%', startangle=140, colors=colors2)
    
    plt.tight_layout()
    plt.suptitle('Blood Type Distribution Comparison', fontsize=16)
    plt.subplots_adjust(top=0.85)
    plt.show()

    


    
    

if __name__ == "__main__":
    main()