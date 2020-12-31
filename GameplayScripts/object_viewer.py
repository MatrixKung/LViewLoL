from lview import *
from pprint import pprint

lview_script_info = {
	"script": "Object Explorer",
	"author": "leryss",
	"description": "Provides a way to explore in game objects"
}

def draw_spell(spell, ui):
	
	if ui.treenode(str(spell.slot)):
		ui.labeltext("name", spell.name)
		ui.labeltext("summmoner_spell_type", str(spell.summoner_spell_type))
		ui.dragint("level", spell.level)
		ui.dragfloat("ready_at", spell.ready_at)
		ui.dragfloat("value", spell.value)
		
		ui.treepop()
		
def draw_items(items, ui):
	for item in items:
		if item != None and ui.treenode(str(item.id)):
			
			if item.movement_speed > 0:         ui.dragfloat("movement_speed", item.movement_speed) 
			if item.health > 0:                 ui.dragfloat("health", item.health)                                 
			if item.crit > 0:                   ui.dragfloat("crit", item.crit)                                     
			if item.ability_power > 0:          ui.dragfloat("ability_power", item.ability_power)                  
			if item.mana > 0:                   ui.dragfloat("mana", item.mana)                                     
			if item.armour > 0:                 ui.dragfloat("armour", item.armour)                                 
			if item.magic_resist > 0:           ui.dragfloat("magic_resist", item.magic_resist)                     
			if item.physical_damage > 0:        ui.dragfloat("physical_damage", item.physical_damage)               
			if item.attack_speed > 0:           ui.dragfloat("attack_speed", item.attack_speed)                     
			if item.life_steal > 0:             ui.dragfloat("life_steal", item.life_steal)                         
			if item.hp_regen > 0:               ui.dragfloat("hp_regen", item.hp_regen)                             
			if item.movement_speed_percent > 0: ui.dragfloat("movement_speed_percent", item.movement_speed_percent) 

			ui.treepop()

def draw_missile(obj, ui):
	pass
	if ui.treenode('{}=>{} ({})'.format(obj.src_idx, obj.dest_idx, hex(obj.net_id))):
		ui.treepop()

def draw_game_object(obj, ui, additional_draw = None, set_open=False):
	
	if(obj == None):
		ui.text("null", Color.RED)
		return
	if(set_open):
		ui.opennext()
	if ui.treenode("{}_{}".format(obj.name, obj.id)):
		ui.labeltext("address", hex(obj.address))
		ui.labeltext("name", obj.name, Color.ORANGE)
		ui.labeltext("type", str(obj.type), Color.CYAN)
		ui.labeltext("pos", f"x={obj.pos.x:.2f}, y={obj.pos.y:.2f}, z={obj.pos.z:.2f}")
		ui.dragint("id", obj.id)
		
		ui.separator()
		ui.dragfloat("health", obj.health)
		ui.checkbox("is_alive", obj.is_alive)
		
		ui.separator()
		ui.dragfloat("base_atk", obj.base_atk)
		ui.dragfloat("bonus_atk", obj.bonus_atk)
		ui.dragfloat("armour", obj.armour)
		ui.dragfloat("magic_resist", obj.magic_resist)
		ui.dragfloat("ap", obj.ap)
		ui.dragfloat("bonus_ap", obj.bonus_ap)
		ui.dragfloat("crit", obj.crit)
		ui.dragfloat("crit_multi", obj.crit_multi)
		
		ui.separator()
		ui.dragfloat("base_atk_range", obj.base_atk_range)
		ui.dragfloat("base_atk_speed", obj.base_atk_speed)
		ui.dragfloat("max_atk_speed", obj.max_atk_speed)
		ui.dragfloat("atk_speed_multi", obj.atk_speed_multi)
		
		ui.separator()
		ui.dragfloat("target_radius", obj.target_radius)
		ui.dragfloat("gameplay_radius", obj.gameplay_radius)
		
		ui.separator()
		ui.dragfloat("duration", obj.duration)
		ui.dragfloat("last_visible_at", obj.last_visible_at)
		ui.checkbox("is_visible", obj.is_visible)
		
		if additional_draw != None:
			additional_draw()
		
		ui.treepop()
	
def draw_champion(obj, ui):
	def draw_spells():
		ui.dragint("Level", obj.lvl)
			
		ui.text("Items")
		draw_items(obj.items, ui)
		
		ui.text("Skills")
		draw_spell(obj.Q, ui)
		draw_spell(obj.W, ui)
		draw_spell(obj.E, ui)
		draw_spell(obj.R, ui)
		draw_spell(obj.D, ui)
		draw_spell(obj.F, ui)
		
	draw_game_object(obj, ui, additional_draw = draw_spells)
	
def draw_list(label, objs, ui, draw_func):
	if ui.treenode(label):
		for obj in objs:
			draw_func(obj, ui)
		ui.treepop()
	
def lview_load_cfg(cfg):
	pass
	
def lview_save_cfg(cfg):
	pass
	
def lview_draw_settings(objs, ui):
	pass
	
def lview_update(game, ui):
	
	ui.begin("Object Viewer")
	
	ui.dragfloat("time", game.time)
	ui.text("Hovered Object")
	draw_game_object(game.hovered_obj, ui, set_open=True)
	
	ui.text("Local Champion")
	draw_champion(game.local_champ, ui)
	
	ui.text("Lists")
	draw_list("Champions", game.champs,    ui, draw_champion)
	draw_list("Minions",   game.minions,   ui, draw_game_object)
	draw_list("Jungle",    game.jungle,    ui, draw_game_object)
	draw_list("Turrets",   game.turrets,   ui, draw_game_object)
	draw_list("Missiles",  game.missiles,  ui, draw_missile)
	draw_list("Others",    game.others,    ui, draw_game_object)

	
	ui.end()
	