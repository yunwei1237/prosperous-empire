@echo off
python src/process_init.py
python src/process_global_variables.py
python src/process_strings.py
python src/process_skills.py
python src/process_music.py
python src/process_animations.py
python src/process_meshes.py
python src/process_sounds.py
python src/process_skins.py
python src/process_map_icons.py
python src/process_factions.py
python src/process_items.py
python src/process_scenes.py
python src/process_troops.py
python src/process_particle_sys.py
python src/process_scene_props.py
python src/process_tableau_materials.py
python src/process_presentations.py
python src/process_party_tmps.py
python src/process_parties.py
python src/process_quests.py
python src/process_info_pages.py
python src/process_scripts.py
python src/process_mission_tmps.py
python src/process_game_menus.py
python src/process_simple_triggers.py
python src/process_dialogs.py
python src/process_global_variables_unused.py
python src/process_postfx.py

::del src/*.pyc

echo.
echo ______________________________
echo.
echo Script src/processing has ended.
echo Press any key to exit. . .

:: pause>nul