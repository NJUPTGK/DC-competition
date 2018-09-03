import pandas as pd
import numpy as np
from datetime import date
game_train = pd.read_csv('tap_fun_train.csv')
#game_test = pd.read_csv('tap_fun_test.csv')
feature3 = game_train[((game_train.date>='20160315')&(game_train.date<='20160630'))|((game_train.date=='null')&(game_train.date_received>='20160315')&(game_train.date_received<='20160630'))]
dataset2 = game_train[(game_train.date_received>='20160515')&(game_train.date_received<='20160615')]
feature2 = game_train[(game_train.date>='20160201')&(game_train.date<='20160514')|((game_train.date=='null')&(game_train.date_received>='20160201')&(game_train.date_received<='20160514'))]
dataset1 = game_train[(game_train.date_received>='20160414')&(game_train.date_received<='20160514')]
feature1 = game_train[(game_train.date>='20160101')&(game_train.date<='20160413')|((game_train.date=='null')&(game_train.date_received>='20160101')&(game_train.date_received<='20160413'))]
#for game_train
t = game_train[['user_id','wood_add_value','wood_reduce_value']]
if t.wood_add_value.any()!=0:
    t['wood_reduce_add']=t.wood_reduce_value/t.wood_add_value
else:
    t['wood_reduce_add']=0
t=t.drop(['wood_add_value','wood_reduce_value'],axis=1)

t1 = game_train[['user_id','stone_add_value','stone_reduce_value']]
if t1.stone_add_value.any()!=0:
    t1['stone_reduce_add']=t1.stone_reduce_value/t1.stone_add_value
else:
    t1['stone_reduce_add']=0
t1=t1.drop(['stone_add_value','stone_reduce_value'],axis=1)

t2 = game_train[['user_id','ivory_add_value','ivory_reduce_value']]
if t2.ivory_add_value.any()!=0:
    t2['ivory_reduce_add']=t2.ivory_reduce_value/t2.ivory_add_value
else:
    t2['ivory_reduce_add']=0
t2=t2.drop(['ivory_add_value','ivory_reduce_value'],axis=1)

t3 = game_train[['user_id','meat_add_value','meat_reduce_value']]
if t3.meat_add_value.any()!=0:
    t3['meat_reduce_add']=t3.meat_reduce_value/t3.meat_add_value
else:
    t3['meat_reduce_add']=0
t3=t3.drop(['meat_add_value','meat_reduce_value'],axis=1)

t4 = game_train[['user_id','magic_add_value','magic_reduce_value']]
if t4.magic_add_value.any()!=0:
    t4['magic_reduce_add']=t4.magic_reduce_value/t4.magic_add_value
else:
    t4['magic_reduce_add']=0
t4=t4.drop(['magic_add_value','magic_reduce_value'],axis=1)

t5 = game_train[['user_id','infantry_add_value','infantry_reduce_value']]
if t5.infantry_add_value.any()!=0:
    t5['infantry_reduce_add']=t5.infantry_reduce_value/t5.infantry_add_value
else:
    t5['infantry_reduce_add']=0
t5=t5.drop(['infantry_add_value','infantry_reduce_value'],axis=1)

t6 = game_train[['user_id','cavalry_add_value','cavalry_reduce_value']]
if t6.cavalry_add_value.any()!=0:
    t6['cavalry_reduce_add']=t6.cavalry_reduce_value/t6.cavalry_add_value
else:
    t6['cavalry_reduce_add']=0
t6=t6.drop(['cavalry_add_value','cavalry_reduce_value'],axis=1)

t7 = game_train[['user_id','shaman_add_value','shaman_reduce_value']]
if t7.shaman_add_value.any()!=0:
    t7['shaman_reduce_add']=t7.shaman_reduce_value/t7.shaman_add_value
else:
    t7['shaman_reduce_add']=0
t7=t7.drop(['shaman_add_value','shaman_reduce_value'],axis=1)

t8 = game_train[['user_id','wound_infantry_add_value','wound_infantry_reduce_value']]
if t8.wound_infantry_add_value.any()!=0:
    t8['wound_infantry_reduce_add']=t8.wound_infantry_reduce_value/t8.wound_infantry_add_value
else:
    t8['wound_infantry_reduce_add']=0
t8=t8.drop(['wound_infantry_add_value','wound_infantry_reduce_value'],axis=1)

t9 = game_train[['user_id','wound_cavalry_add_value','wound_cavalry_reduce_value']]
if t9.wound_cavalry_add_value.any()!=0:
    t9['wound_cavalry_reduce_add']=t9.wound_cavalry_reduce_value/t9.wound_cavalry_add_value
else:
    t9['wound_cavalry_reduce_add']=0
t9=t9.drop(['wound_cavalry_add_value','wound_cavalry_reduce_value'],axis=1)

t10 = game_train[['user_id','wound_shaman_add_value','wound_shaman_reduce_value']]
if t10.wound_shaman_add_value.any()!=0:
    t10['wound_shaman_reduce_add']=t10.wound_shaman_reduce_value/t10.wound_shaman_add_value
else:
    t10['wound_shaman_reduce_add']=0
t10=t10.drop(['wound_shaman_add_value','wound_shaman_reduce_value'],axis=1)

t11 = game_train[['user_id','general_acceleration_add_value','general_acceleration_reduce_value']]
if t11.general_acceleration_add_value.any()!=0:
    t11['general_acceleration_reduce_add']=t11.general_acceleration_reduce_value/t11.general_acceleration_add_value
else:
    t11['general_acceleration_reduce_add']=0
t11=t11.drop(['general_acceleration_add_value','general_acceleration_reduce_value'],axis=1)

t12 = game_train[['user_id','building_acceleration_add_value','building_acceleration_reduce_value']]
if t12.building_acceleration_add_value.any()!=0:
    t12['building_acceleration_reduce_add']=t12.building_acceleration_reduce_value/t12.building_acceleration_add_value
else:
    t12['building_acceleration_reduce_add']=0
t12=t12.drop(['building_acceleration_add_value','building_acceleration_reduce_value'],axis=1)

t13 = game_train[['user_id','reaserch_acceleration_add_value','reaserch_acceleration_reduce_value']]
if t13.reaserch_acceleration_add_value.any()!=0:
    t13['reaserch_acceleration_reduce_add']=t13.reaserch_acceleration_reduce_value/t13.reaserch_acceleration_add_value
else:
    t13['reaserch_acceleration_reduce_add']=0
t13=t13.drop(['reaserch_acceleration_add_value','reaserch_acceleration_reduce_value'],axis=1)

t14 = game_train[['user_id','training_acceleration_add_value','training_acceleration_reduce_value']]
if t14.training_acceleration_add_value.any()!=0:
    t14['training_acceleration_reduce_add']=t14.training_acceleration_reduce_value/t14.training_acceleration_add_value
else:
    t14['training_acceleration_reduce_add']=0
t14=t14.drop(['training_acceleration_add_value','training_acceleration_reduce_value'],axis=1)

t15 = game_train[['user_id','treatment_acceleraion_add_value','treatment_acceleration_reduce_value']]
if t15.treatment_acceleraion_add_value.any()!=0:
    t15['treatment_acceleration_reduce_add']=t15.treatment_acceleraion_add_value/t15.treatment_acceleration_reduce_value
else:
    t15['treatment_acceleration_reduce_add']=0
t15=t15.drop(['treatment_acceleraion_add_value','treatment_acceleration_reduce_value'],axis=1)

dataset1 = pd.merge(t1,t,on='user_id')
dataset1 = pd.merge(dataset1,t2,on='user_id')
dataset1 = pd.merge(dataset1,t3,on='user_id')
dataset1 = pd.merge(dataset1,t4,on='user_id')
dataset1 = pd.merge(dataset1,t5,on='user_id')
dataset1 = pd.merge(dataset1,t6,on='user_id')
dataset1 = pd.merge(dataset1,t7,on='user_id')
dataset1 = pd.merge(dataset1,t8,on='user_id')
dataset1 = pd.merge(dataset1,t9,on='user_id')
dataset1 = pd.merge(dataset1,t10,on='user_id')
dataset1 = pd.merge(dataset1,t11,on='user_id')
dataset1 = pd.merge(dataset1,t12,on='user_id')
dataset1 = pd.merge(dataset1,t13,on='user_id')
dataset1 = pd.merge(dataset1,t14,on='user_id')
dataset1 = pd.merge(dataset1,t15,on='user_id')
dataset1.replace(np.nan,0,inplace=True)
dataset1.replace(np.inf,0,inplace=True)
dataset1.to_csv('dataset1.csv',index=None)
print(dataset1.shape)
#m = game_train[['user_id','bd_training_hut_level','bd_healing_lodge_level','bd_stronghold_level','bd_outpost_portal_level','bd_barrack_level','bd_healing_spring_level','bd_dolmen_level','bd_guest_cavern_level','bd_warehouse_level','bd_watchtower_level','bd_magic_coin_tree_level','bd_hall_of_war_level','bd_market_level','bd_hero_gacha_level','bd_hero_strengthen_level','bd_hero_pve_level','sr_scout_level','sr_training_speed_level','sr_infantry_tier_2_level','sr_cavalry_tier_2_level','sr_shaman_tier_2_level','sr_infantry_atk_level','sr_cavalry_atk_level','sr_shaman_atk_level','sr_infantry_tier_3_level','sr_cavalry_tier_3_level','sr_shaman_tier_3_level','sr_troop_defense_level','sr_infantry_def_level'
  # ,'sr_cavalry_def_level','sr_shaman_def_level','sr_infantry_hp_level'
  #  ,'sr_cavalry_hp_level','sr_shaman_hp_level','sr_infantry_tier_4_level'
  #  ,'sr_cavalry_tier_4_level','sr_shaman_tier_4_level','sr_troop_attack_level'
  # ,'sr_construction_speed_level','sr_hide_storage_level','sr_troop_consumption_level'
  #  ,'sr_rss_a_prod_levell','sr_rss_b_prod_level','sr_rss_c_prod_level','sr_rss_d_prod_level','sr_rss_a_gather_level','sr_rss_b_gather_level','sr_rss_c_gather_level','sr_rss_d_gather_level','sr_troop_load_level','sr_rss_e_gather_level','sr_rss_e_prod_level','sr_outpost_durability_level','sr_outpost_tier_2_level','sr_healing_space_level','sr_gathering_hunter_buff_level','sr_healing_speed_level','sr_outpost_tier_3_level','sr_alliance_march_speed_level','sr_pvp_march_speed_level','sr_gathering_march_speed_level','sr_outpost_tier_4_level','sr_guest_troop_capacity_level','sr_march_size_level','sr_rss_help_bonus_level']]

#dataset2 = m
#dataset2.to_csv('dataset2.csv',index = None)
#print(dataset2.shape)
h = game_train[['user_id','pvp_battle_count','pvp_lanch_count','pvp_win_count']]
if h.pvp_battle_count.any()!=0:
    h['pvp_lanch_battle']=h.pvp_lanch_count/h.pvp_battle_count
    h['pvp_win_battle']=h.pvp_win_count/h.pvp_battle_count
    if h.pvp_lanch_count.any()!=0:
        h['pvp_win_lanch']=h.pvp_win_count/h.pvp_lanch_count
else:
    h['pvp_lanch_battle'] = 0
    h['pvp_win_battle'] = 0
    h['pvp_win_lanch'] = 0

h1 = game_train[['user_id','pve_battle_count','pve_lanch_count','pve_win_count']]
if h1.pve_battle_count.any()!=0:
    h1['pve_lanch_battle']=h1.pve_lanch_count/h1.pve_battle_count
    h1['pve_win_battle']=h1.pve_win_count/h1.pve_battle_count
    if h1.pve_lanch_count.any()!=0:
        h1['pve_win_lanch']=h1.pve_win_count/h1.pve_lanch_count
else:
    h1['pve_lanch_battle'] = 0
    h1['pve_win_battle'] = 0
    h1['pve_win_lanch'] = 0

h2 = game_train[['user_id','avg_online_minutes','pay_price','pay_count','prediction_pay_price']]
dataset3 = pd.merge(h,h1,on='user_id')
dataset3 = pd.merge(dataset3,h2,on='user_id')
dataset3.replace(np.nan,0,inplace=True)
dataset3.replace(np.inf,0,inplace=True)
dataset3.to_csv('dataset3.csv',index=None)
print(dataset3.shape)
data1 = pd.read_csv('dataset1.csv')
#data2 = pd.read_csv('dataset2.csv')
data3 = pd.read_csv('dataset3.csv')
test = pd.merge(data1,data3,on='user_id')
#test = pd.merge(test,data3,on='user_id')
print(test.shape)
test.to_csv('train.csv',index=None)
