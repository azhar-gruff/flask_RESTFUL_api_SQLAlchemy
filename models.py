# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Integer, Table, Unicode
from sqlalchemy.dialects.mssql import BIT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_CTREE = Table(
    'CTREE', metadata,
    Column('親会社DUNSナンバー', Unicode(9)),
    Column('親会社商号漢字', Unicode(255)),
    Column('親会社商号カタカナインデックス', Unicode(255)),
    Column('DUNSナンバー', Unicode(9)),
    Column('企業商号漢字', Unicode(255)),
    Column('企業商号カタカナインデックス', Unicode(255)),
    Column('証券コード', Unicode(6)),
    Column('会社区分', Unicode(2)),
    Column('企業所在地', Unicode(255)),
    Column('資本金', Unicode(255)),
    Column('営業種目名称', Unicode(255)),
    Column('所有議決権（直接）', Unicode(11)),
    Column('所有議決権（間接）', Unicode(11)),
    Column('所有議決権（合計）', Unicode(11)),
    Column('役員・当社役員', Unicode(11)),
    Column('役員・当社従業員（職員）', Unicode(11)),
    Column('事実上関係', Unicode(255)),
    Column('備考', Unicode(255)),
    Column('国内外企業区分', Unicode(1)),
    Column('上場区分', Unicode(1)),
    Column('連結決算年', Unicode(4)),
    Column('連結決算月', Unicode(2)),
    schema='company'
)


t_Mst_address = Table(
    'Mst_address', metadata,
    Column('postal_code', Unicode(7), nullable=False),
    Column('prefecture', Unicode(8), nullable=False),
    Column('city', Unicode(30), nullable=False),
    schema='company'
)


t_RiskscoreReason = Table(
    'RiskscoreReason', metadata,
    Column('D-U-N-S®Number', Unicode(20)),
    Column('リスクスコア（スコアパーセンタイル）', Unicode(20)),
    Column('リスクスコア全平均', Unicode(20)),
    Column('リスクスコア業種平均', Unicode(20)),
    Column('倒産確率', Unicode(20)),
    Column('ロースコア', Unicode(20)),
    Column('リスククラス', Unicode(20)),
    Column('リスクスコア算出日', Unicode(20)),
    Column('リーズンコード1', Unicode(100)),
    Column('リーズンコード2', Unicode(100)),
    Column('リーズンコード3', Unicode(100)),
    Column('リーズンコード4', Unicode(100)),
    Column('リーズンコード5', Unicode(100)),
    schema='company'
)


t_TSR = Table(
    'TSR', metadata,
    Column('メンテナンス区分', Unicode(1)),
    Column('企業コード', Unicode(9)),
    Column('法人格前後区分', Unicode(1)),
    Column('法人格略コード', Unicode(2)),
    Column('商号外字フラグ', Unicode(1)),
    Column('商号オーバーフラグ', Unicode(1)),
    Column('漢字商号', Unicode(120)),
    Column('インデックス漢字商号', Unicode(40)),
    Column('余白１', Unicode(120)),
    Column('カナ商号', Unicode(120)),
    Column('インデックスカナ商号', Unicode(40)),
    Column('Ｔｓｒ住所コード', Unicode(9)),
    Column('Ｊｉｓ住所コード', Unicode(5)),
    Column('企業郵便番号', Unicode(8)),
    Column('企業所在地桁数', Unicode(11)),
    Column('住所外字フラグ', Unicode(1)),
    Column('企業所在地', Unicode(200)),
    Column('企業電話番号', Unicode(15)),
    Column('余白２', Unicode(15)),
    Column('倒産フラグ', Unicode(1)),
    Column('評点', Unicode(2)),
    Column('上場区分', Unicode(1)),
    Column('株式コード', Unicode(4)),
    Column('Ｅｄｉｎｅｔコード', Unicode(6)),
    Column('創業年月西暦年月', Unicode(6)),
    Column('明治以前創業年', Unicode(12)),
    Column('設立年月西暦年月', Unicode(6)),
    Column('資本金千円', Unicode(10)),
    Column('従業員数', Unicode(6)),
    Column('一株金額', Unicode(7)),
    Column('工場数', Unicode(2)),
    Column('事業所数', Unicode(3)),
    Column('銀行コード１', Unicode(7)),
    Column('銀行コード２', Unicode(7)),
    Column('銀行コード３', Unicode(7)),
    Column('銀行コード４', Unicode(7)),
    Column('銀行コード５', Unicode(7)),
    Column('銀行コード６', Unicode(7)),
    Column('銀行コード７', Unicode(7)),
    Column('銀行コード８', Unicode(7)),
    Column('銀行コード９', Unicode(7)),
    Column('銀行コード１０', Unicode(7)),
    Column('銀行名称１', Unicode(30)),
    Column('銀行名称１店舗名', Unicode(30)),
    Column('銀行名称２', Unicode(30)),
    Column('銀行名称２店舗名', Unicode(30)),
    Column('銀行名称３', Unicode(30)),
    Column('銀行名称３店舗名', Unicode(30)),
    Column('銀行名称４', Unicode(30)),
    Column('銀行名称４店舗名', Unicode(30)),
    Column('銀行名称５', Unicode(30)),
    Column('銀行名称５店舗名', Unicode(30)),
    Column('銀行名称６', Unicode(30)),
    Column('銀行名称６店舗名', Unicode(30)),
    Column('銀行名称７', Unicode(30)),
    Column('銀行名称７店舗名', Unicode(30)),
    Column('銀行名称８', Unicode(30)),
    Column('銀行名称８店舗名', Unicode(30)),
    Column('銀行名称９', Unicode(30)),
    Column('銀行名称９店舗名', Unicode(30)),
    Column('銀行名称１０', Unicode(30)),
    Column('銀行名称１０店舗名', Unicode(30)),
    Column('業種コード１主', Unicode(4)),
    Column('業種コード２従', Unicode(4)),
    Column('業種コード３従', Unicode(4)),
    Column('業種名称１主', Unicode(64)),
    Column('業種名称２従', Unicode(64)),
    Column('業種名称３従', Unicode(64)),
    Column('扱い品コード１', Unicode(6)),
    Column('扱い品コード２', Unicode(6)),
    Column('扱い品コード３', Unicode(6)),
    Column('扱い品コード４', Unicode(6)),
    Column('扱い品コード５', Unicode(6)),
    Column('扱い品コード６', Unicode(6)),
    Column('扱い品名称１', Unicode(120)),
    Column('扱い品名称２', Unicode(120)),
    Column('扱い品名称３', Unicode(120)),
    Column('扱い品名称４', Unicode(120)),
    Column('扱い品名称５', Unicode(120)),
    Column('扱い品名称６', Unicode(120)),
    Column('営業種目名外字フラグ', Unicode(1)),
    Column('営業種目名称', Unicode(224)),
    Column('役員名称外字フラグ', Unicode(1)),
    Column('役員名称', Unicode(224)),
    Column('大株主名称外字フラグ', Unicode(1)),
    Column('大株主名称', Unicode(224)),
    Column('仕入先名称外字フラグ', Unicode(1)),
    Column('仕入先名称', Unicode(224)),
    Column('販売先名称外字フラグ', Unicode(1)),
    Column('販売先名称', Unicode(224)),
    Column('支店名称外字フラグ', Unicode(1)),
    Column('工場支店営業所名称', Unicode(336)),
    Column('概況外字フラグ', Unicode(1)),
    Column('概況', Unicode(240)),
    Column('前々期決算決算年月', Unicode(6)),
    Column('前々期決算月数', Unicode(2)),
    Column('前々期売上高千円', Unicode(12)),
    Column('前々期税込引区分', Unicode(1)),
    Column('前々期利益金千円', Unicode(12)),
    Column('前々期決算配当', Unicode(3)),
    Column('余白３', Unicode(1)),
    Column('前々期財務有無フラグ', Unicode(1)),
    Column('余白４', Unicode(10)),
    Column('前期決算決算年月', Unicode(6)),
    Column('前期決算月数', Unicode(2)),
    Column('前期売上高千円', Unicode(12)),
    Column('前期決算税込引区分', Unicode(1)),
    Column('前期利益金千円', Unicode(12)),
    Column('前期決算配当', Unicode(3)),
    Column('余白５', Unicode(1)),
    Column('前期財務有無フラグ', Unicode(1)),
    Column('余白６', Unicode(10)),
    Column('当期決算決算年月', Unicode(6)),
    Column('当期決算月数', Unicode(2)),
    Column('当期売上高千円', Unicode(12)),
    Column('当期決算税込引区分', Unicode(1)),
    Column('当期利益金千円', Unicode(12)),
    Column('当期決算配当', Unicode(3)),
    Column('余白７', Unicode(1)),
    Column('当期財務有無フラグ', Unicode(1)),
    Column('余白８', Unicode(10)),
    Column('当期売上伸長率', Unicode(4)),
    Column('当期売上伸長額千円', Unicode(12)),
    Column('前期売上伸長率', Unicode(4)),
    Column('前期売上伸長額千円', Unicode(12)),
    Column('当期利益伸長率', Unicode(6)),
    Column('当期利益伸長額千円', Unicode(12)),
    Column('前期利益伸長率', Unicode(6)),
    Column('前期利益伸長額千円', Unicode(12)),
    Column('一人月間売上金額千円', Unicode(9)),
    Column('一人月間利益金額千円', Unicode(9)),
    Column('余白９', Unicode(6)),
    Column('代表者氏名外字フラグ', Unicode(1)),
    Column('代表者氏名ｏｖフラグ', Unicode(1)),
    Column('代表者氏名', Unicode(60)),
    Column('余白１０', Unicode(20)),
    Column('代表者氏名カナ', Unicode(32)),
    Column('生年月日西暦', Unicode(8)),
    Column('男女区分', Unicode(1)),
    Column('干支コード', Unicode(2)),
    Column('干支名称', Unicode(4)),
    Column('役職コード', Unicode(2)),
    Column('役職名称', Unicode(24)),
    Column('代表者ｔｓｒ住所ｃｄ', Unicode(9)),
    Column('代表者ｊｉｓ住所ｃｄ', Unicode(5)),
    Column('代表者郵便番号', Unicode(8)),
    Column('代表者住所桁数', Unicode(11)),
    Column('代表者住所外字フラグ', Unicode(1)),
    Column('代表者現住所', Unicode(200)),
    Column('代表者電話番号', Unicode(15)),
    Column('出身地コード', Unicode(2)),
    Column('出身地名称', Unicode(20)),
    Column('住居コード', Unicode(1)),
    Column('住居名称', Unicode(24)),
    Column('最終学歴学校コード', Unicode(4)),
    Column('最終学歴学校名称', Unicode(120)),
    Column('卒業区分', Unicode(1)),
    Column('趣味コード１', Unicode(2)),
    Column('趣味コード２', Unicode(2)),
    Column('趣味コード３', Unicode(2)),
    Column('趣味名称１', Unicode(18)),
    Column('趣味名称２', Unicode(18)),
    Column('趣味名称３', Unicode(18)),
    Column('倒産経歴', Unicode(1)),
    Column('納税年西暦', Unicode(4)),
    Column('納税額千円', Unicode(9)),
    Column('企業所在地バーコード', Unicode(23)),
    Column('代表者現住所バーｃｄ', Unicode(23)),
    Column('余白１１', Unicode(28)),
    Column('Ｄｕｎｓナンバー', Unicode(9)),
    Column('法人番号', Unicode(13)),
    schema='company'
)


class BankrupcyReasonMst(Base):
    __tablename__ = 'bankrupcy_reason_mst'
    __table_args__ = {'schema': 'company'}

    graph_id_B3CCB33CE8DD4FAF83223C759723C28A = Column(BigInteger, nullable=False, unique=True)
    _node_id_643894828D0E43F29855BFB6B561FC86 = Column('$node_id_643894828D0E43F29855BFB6B561FC86', Unicode(1000), nullable=False)
    bankrupcy_reason_code = Column(Unicode(2), primary_key=True)
    bankrupcy_reason = Column(Unicode(50))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class BankruptcyMst(Base):
    __tablename__ = 'bankruptcy_mst'
    __table_args__ = {'schema': 'company'}

    graph_id_D00005AE99FC4DFD9B45ED650A2EAE2F = Column(BigInteger, nullable=False, unique=True)
    _node_id_D74FAF5E8CBC44679044791DDED86177 = Column('$node_id_D74FAF5E8CBC44679044791DDED86177', Unicode(1000), nullable=False)
    company_code = Column(Unicode(15), primary_key=True, nullable=False)
    bankrupcy_date = Column(Date, primary_key=True, nullable=False)
    bankrupcy_reason_code = Column(Unicode(2))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class CompanyBase(Base):
    __tablename__ = 'company_base'
    __table_args__ = {'schema': 'company'}

    graph_id_5A774606EB94428B817BA4F81D9D13E5 = Column(BigInteger, nullable=False, unique=True)
    _node_id_0E31766DB9FA404F96464780D4D75E67 = Column('$node_id_0E31766DB9FA404F96464780D4D75E67', Unicode(1000), nullable=False)
    company_code = Column(Unicode(15), primary_key=True, nullable=False)
    company_base_code = Column(Unicode(4), primary_key=True, nullable=False)
    base_duns_no = Column(Unicode(15))
    base_name = Column(Unicode(50))
    base_type_code = Column(Unicode(2))
    tsr_street_address_code = Column(Unicode(15))
    jis_street_address_code = Column(Unicode(15))
    postal_code = Column(Unicode(15))
    prefecture = Column(Unicode(50))
    city = Column(Unicode(50))
    city_region = Column(Unicode(50))
    chome = Column(Unicode(50))
    street_address_other = Column(Unicode(50))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class CompanyBaseCodeMapping(Base):
    __tablename__ = 'company_base_code_mapping'
    __table_args__ = {'schema': 'company'}

    company_code = Column(Unicode(15), primary_key=True, nullable=False)
    company_base_code = Column(Unicode(4), primary_key=True, nullable=False)
    base_duns_no = Column(Unicode(15))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class CompanyClassMst(Base):
    __tablename__ = 'company_class_mst'
    __table_args__ = {'schema': 'company'}

    graph_id_31BF340E0D514E20B9C75EA4E9E80A5B = Column(BigInteger, nullable=False, unique=True)
    _node_id_F9D0C5FF656740E7A9AC9C80BE0D7865 = Column('$node_id_F9D0C5FF656740E7A9AC9C80BE0D7865', Unicode(1000), nullable=False)
    company_class_code = Column(Unicode(2), primary_key=True)
    company_class_name = Column(Unicode(10))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class CompanyCodeMapping(Base):
    __tablename__ = 'company_code_mapping'
    __table_args__ = {'schema': 'company'}

    company_code = Column(Unicode(15), primary_key=True)
    duns_no = Column(Unicode(15))
    company_unity_code = Column(Unicode(15))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class CompanyIndustry(Base):
    __tablename__ = 'company_industry'
    __table_args__ = {'schema': 'company'}

    graph_id_49D0AA648B594F6CAAD2DAA1E6E01F72 = Column(BigInteger, nullable=False, unique=True)
    _node_id_8DC31064D28941D1BCE86B161FDA02B8 = Column('$node_id_8DC31064D28941D1BCE86B161FDA02B8', Unicode(1000), nullable=False)
    company_code = Column(Unicode(15), primary_key=True, nullable=False)
    industry_code = Column(Unicode(15), primary_key=True, nullable=False)
    main_flg = Column(BIT)
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class CompanyMst(Base):
    __tablename__ = 'company_mst'
    __table_args__ = {'schema': 'company'}

    graph_id_D0AE49CA2EC8472AA5588DCEA19680B7 = Column(BigInteger, nullable=False, unique=True)
    _node_id_C4F3D7691EF64346B2263F516139551E = Column('$node_id_C4F3D7691EF64346B2263F516139551E', Unicode(1000), nullable=False)
    company_code = Column(Unicode(15), primary_key=True)
    duns_no = Column(Unicode(15))
    company_name = Column(Unicode(50))
    company_name_kana = Column(Unicode(100))
    capital = Column(Integer)
    estabishment_year_month = Column(Unicode(7))
    found_year_month = Column(Unicode(7))
    employee_count = Column(Integer)
    settlement_month_two_years_ago = Column(Unicode(7))
    company_sales_two_years_ago = Column(BigInteger)
    company_profit_two_years_ago = Column(Integer)
    settlement_month_one_year_ago = Column(Unicode(7))
    company_sales_one_year_ago = Column(BigInteger)
    company_profit_one_year_ago = Column(Integer)
    settlement_month_leatest = Column(Unicode(7))
    company_sales_leatest = Column(BigInteger)
    company_profit_leatest = Column(Integer)
    representative_name = Column(Unicode(50))
    representative_name_kana = Column(Unicode(50))
    representative_tel_no = Column(Unicode(15))
    general_company_class_code = Column(Unicode(2))
    sb_company_class_code = Column(Unicode(2))
    company_risk_score = Column(Integer)
    sb_org_company_risk_score = Column(Integer)
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class CompanyRelationMst(Base):
    __tablename__ = 'company_relation_mst'
    __table_args__ = {'schema': 'company'}

    graph_id_AF312FF4FFDB4676AE93F6F5C63656A3 = Column(BigInteger, nullable=False, unique=True)
    _node_id_B20B2B3AFDC24FEEB2547B1BD74132D1 = Column('$node_id_B20B2B3AFDC24FEEB2547B1BD74132D1', Unicode(1000), nullable=False)
    relation_code = Column(Unicode(2), primary_key=True)
    relation_name = Column(Unicode(50))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class ContractBannedMst(Base):
    __tablename__ = 'contract_banned_mst'
    __table_args__ = {'schema': 'company'}

    graph_id_5DBA55D2BC53401984EFDBC5C9BAB5B4 = Column(BigInteger, nullable=False, unique=True)
    _node_id_D665A92F524A4C6AA22AC53B0D180662 = Column('$node_id_D665A92F524A4C6AA22AC53B0D180662', Unicode(1000), nullable=False)
    company_code = Column(Unicode(15), primary_key=True, nullable=False)
    product_code = Column(Unicode(15), primary_key=True, nullable=False)
    banned_start_date = Column(Date, primary_key=True, nullable=False)
    banned_end_date = Column(Date)
    note = Column(Unicode(50))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class Industry(Base):
    __tablename__ = 'industry'
    __table_args__ = {'schema': 'company'}

    graph_id_628EDC12C3C94413B1F75C47FCE0D6BB = Column(BigInteger, nullable=False, unique=True)
    _node_id_3C49F36F78EF490C9B6603048DAD081A = Column('$node_id_3C49F36F78EF490C9B6603048DAD081A', Unicode(1000), nullable=False)
    industry_code = Column(Unicode(15), primary_key=True)
    industry_name = Column(Unicode(50))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class ListingCompany(Base):
    __tablename__ = 'listing_company'
    __table_args__ = {'schema': 'company'}

    graph_id_E7BC2B23ACA8415796451FD8AAC5F9A8 = Column(BigInteger, nullable=False, unique=True)
    _node_id_91304CDC859F41DAA7B5162A3B29BF2E = Column('$node_id_91304CDC859F41DAA7B5162A3B29BF2E', Unicode(1000), nullable=False)
    listing_code = Column(Unicode(15), primary_key=True, nullable=False)
    company_code = Column(Unicode(15), primary_key=True, nullable=False)
    listing_start_date = Column(Date)
    listing_end_date = Column(Date)
    valid_flg = Column(BIT)
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class ListingMst(Base):
    __tablename__ = 'listing_mst'
    __table_args__ = {'schema': 'company'}

    graph_id_71B998EB2CFE4DE98F60C2501717B27E = Column(BigInteger, nullable=False, unique=True)
    _node_id_742BB6FC2AAB4E088B5C0C9A33F4DEE5 = Column('$node_id_742BB6FC2AAB4E088B5C0C9A33F4DEE5', Unicode(1000), nullable=False)
    listing_code = Column(Unicode(15), primary_key=True)
    listing_destination = Column(Unicode(50))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class OfficeDivMst(Base):
    __tablename__ = 'office_div_mst'
    __table_args__ = {'schema': 'company'}

    graph_id_588F9AAD61FF4A73881840124A835C00 = Column(BigInteger, nullable=False, unique=True)
    _node_id_A97896947BA342208DC6BC89EE6643CB = Column('$node_id_A97896947BA342208DC6BC89EE6643CB', Unicode(1000), nullable=False)
    base_type_code = Column(Unicode(2), primary_key=True)
    base_type_name = Column(Unicode(50))
    sb_base_type_code = Column(Unicode(2))
    sb_base_type_name = Column(Unicode(50))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


class RelationCompany(Base):
    __tablename__ = 'relation_company'
    __table_args__ = {'schema': 'company'}

    graph_id_41E73CC5310F46069A4CF4FB53DE203C = Column(BigInteger, nullable=False, unique=True)
    _node_id_9129589C0D5A4F1D8067A708453B641A = Column('$node_id_9129589C0D5A4F1D8067A708453B641A', Unicode(1000), nullable=False)
    company_code = Column(Unicode(15), primary_key=True, nullable=False)
    relation_company_code = Column(Unicode(15), primary_key=True, nullable=False)
    relation_code = Column(Unicode(2))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))


t_事業所 = Table(
    '事業所', metadata,
    Column('企業DUNSナンバー', Unicode(20)),
    Column('事業所DUNSナンバー', Unicode(20)),
    Column('インデックスカナ商号', Unicode(40)),
    Column('余白1', Unicode(30)),
    Column('漢字商号', Unicode(60)),
    Column('事業所名称', Unicode(60)),
    Column('事業所郵便番号', Unicode(7)),
    Column('バーコード番号', Unicode(23)),
    Column('事業所住所コード', Unicode(10)),
    Column('事業所住所', Unicode(100)),
    Column('事業所電話番号', Unicode(13)),
    Column('業種コード１（主）', Unicode(5)),
    Column('業種名称（主）', Unicode(20)),
    Column('従業員数', Unicode(5)),
    Column('余白2', Unicode(10)),
    Column('余白3', Unicode(10)),
    Column('余白4', Unicode(10)),
    Column('事業所区分コード', Unicode(2)),
    Column('株式コード', Unicode(5)),
    Column('余白5', Unicode(30)),
    schema='company'
)


t_会社区分 = Table(
    '会社区分', metadata,
    Column('会社区分', Unicode(2)),
    Column('会社区分名称', Unicode(80)),
    schema='company'
)


t_倒産情報ファイル = Table(
    '倒産情報ファイル', metadata,
    Column('メンテナンス区分', Unicode(1)),
    Column('倒産整理№', Unicode(40)),
    Column('企業コード', Unicode(30)),
    Column('集計年月', Unicode(20)),
    Column('法人格前後区分', Unicode(10)),
    Column('法人格略コード', Unicode(10)),
    Column('漢字商号', Unicode(120)),
    Column('インデックスカナ商号', Unicode(40)),
    Column('企業住所コード', Unicode(10)),
    Column('企業郵便番号', Unicode(40)),
    Column('企業所在地', Unicode(160)),
    Column('設立年月', Unicode(30)),
    Column('倒産発生日', Unicode(40)),
    Column('資本金（千円）', Integer),
    Column('従業員数', Integer),
    Column('負債総額（百万円）', Integer),
    Column('年商(千円)', Unicode(12)),
    Column('倒産原因コード', Unicode(10)),
    Column('財務有無フラグ', Unicode(10)),
    Column('上場区分', Unicode(10)),
    Column('代表者氏名', Unicode(120)),
    Column('生年月日', Unicode(40)),
    Column('倒産形態コード', Unicode(10)),
    Column('業種コード（主）', Unicode(10)),
    Column('業種コード（従）', Unicode(20)),
    Column('業種名称（主）', Unicode(100)),
    Column('業種名称（従）', Unicode(100)),
    Column('銀行コード１', Unicode(30)),
    Column('銀行コード２', Unicode(30)),
    Column('銀行機関名称１', Unicode(120)),
    Column('銀行機関名称２', Unicode(120)),
    Column('非公開フラグ', Unicode(10)),
    Column('余白', Unicode(30)),
    schema='company'
)


t_学校 = Table(
    '学校', metadata,
    Column("DUN'SNO", Unicode(20)),
    Column('学校名カナ', Unicode(80)),
    Column('学校名', Unicode(60)),
    Column('郵便番号', Unicode(7)),
    Column('バーコード', Unicode(50)),
    Column('TSR住所コード', Unicode(20)),
    Column('住所（和文）＿都道府県', Unicode(100)),
    Column('電話番号', Unicode(20)),
    Column('業種コード１（主）', Unicode(20)),
    Column('業種名称（主）', Unicode(20)),
    Column('学生数', Unicode(20)),
    Column('余白', Unicode(40)),
    Column('学長・校長氏名', Unicode(20)),
    schema='company'
)


t_官公庁 = Table(
    '官公庁', metadata,
    Column('DUNSナンバー', Unicode(20)),
    Column('法人格略コード', Unicode(2)),
    Column('インデックスカナ商号', Unicode(40)),
    Column('漢字商号', Unicode(60)),
    Column('企業郵便番号', Unicode(7)),
    Column('企業所在地バーコード情報', Unicode(23)),
    Column('企業TSR住所コード', Unicode(10)),
    Column('漢字所在地', Unicode(100)),
    Column('企業電話番号', Unicode(15)),
    Column('業種コード１（主）', Unicode(5)),
    Column('業種名称', Unicode(20)),
    Column('組織区分', Unicode(1)),
    Column('親団体漢字団体名', Unicode(30)),
    Column('営業種目名称', Unicode(300)),
    Column('従業員数', Unicode(7)),
    Column('設立年', Unicode(4)),
    Column('設立月', Unicode(2)),
    schema='company'
)


t_業種マスタ = Table(
    '業種マスタ', metadata,
    Column('業種コード', Unicode(4)),
    Column('業種名称(カナ)', Unicode(100)),
    Column('業種名称', Unicode(100)),
    schema='company'
)


t_病院 = Table(
    '病院', metadata,
    Column("DUN'SNO", Unicode(20)),
    Column('病院名カナ', Unicode(80)),
    Column('病院名', Unicode(60)),
    Column('郵便番号', Unicode(7)),
    Column('バーコード', Unicode(50)),
    Column('TSR住所コード', Unicode(20)),
    Column('住所（和文）＿都道府県', Unicode(100)),
    Column('電話番号', Unicode(20)),
    Column('業種コード１（主）', Unicode(20)),
    Column('業種名称（主）', Unicode(20)),
    Column('病床数', Unicode(20)),
    Column('余白', Unicode(40)),
    Column('代表者氏名', Unicode(20)),
    schema='company'
)


t_統一企業マスタ情報 = Table(
    '統一企業マスタ情報', metadata,
    Column('統一企業コード', Unicode(255)),
    Column('法人管理番号', Unicode(255)),
    Column('Dunsnumber', Unicode(255)),
    Column('法人格コード', Unicode(255)),
    Column('企業名カナ', Unicode(255)),
    Column('企業名カナ全角', Unicode(255)),
    Column('企業名', Unicode(255)),
    Column('検索用企業名カナ', Unicode(255)),
    Column('検索用企業名カナ全角', Unicode(255)),
    Column('検索用企業名', Unicode(255)),
    Column('郵便番号', Unicode(255)),
    Column('住所', Unicode(255)),
    Column('住所１ 都道府県', Unicode(255)),
    Column('住所２ 市区群町村', Unicode(255)),
    Column('住所３ 字名丁目', Unicode(255)),
    Column('住所４ 番地', Unicode(255)),
    Column('住所５ ビル建物名', Unicode(255)),
    Column('電話番号', Unicode(255)),
    Column('主業コード', Unicode(255)),
    Column('従業コード', Unicode(255)),
    Column('代表者役職名', Unicode(255)),
    Column('代表者氏名カナ', Unicode(255)),
    Column('代表者氏名カナ全角', Unicode(255)),
    Column('代表者氏名', Unicode(255)),
    Column('主業名', Unicode(255)),
    Column('従業名', Unicode(255)),
    Column('組織区分', Unicode(255)),
    Column('事業内容', Unicode(255)),
    Column('重要度ランク', Unicode(255)),
    Column('証券コード', Unicode(255)),
    Column('Ｕｒｌ', Unicode(255)),
    Column('合併企業番号', Unicode(255)),
    Column('親企業フラグ', Unicode(255)),
    Column('親企業番号', Unicode(255)),
    Column('Sb業種大', Unicode(255)),
    Column('Sb業種中', Unicode(255)),
    Column('Sb業種小', Unicode(255)),
    Column('備考1', Unicode(255)),
    Column('備考2', Unicode(255)),
    Column('備考3', Unicode(255)),
    Column('備考4', Unicode(255)),
    Column('備考5', Unicode(255)),
    Column('有効無効フラグ', Unicode(255)),
    Column('無効理由', Unicode(255)),
    Column('登録日', Unicode(255)),
    Column('更新日', Unicode(255)),
    Column('登録者', Unicode(255)),
    Column('更新者', Unicode(255)),
    Column('削除フラグ', Unicode(255)),
    Column('登録日時', Unicode(255)),
    Column('更新日時', Unicode(255)),
    Column('登録者名', Unicode(255)),
    Column('更新者名', Unicode(255)),
    Column('Data Universal Number', Unicode(255)),
    Column('Mnc Management Name', Unicode(255)),
    Column('Postal Code', Unicode(255)),
    Column('Country Code', Unicode(255)),
    Column('City', Unicode(255)),
    Column('Country Calling Code', Unicode(255)),
    Column('District', Unicode(255)),
    Column('現地法人名 日本語', Unicode(255)),
    Column('Customer Name', Unicode(255)),
    Column('備考', Unicode(255)),
    schema='company'
)
