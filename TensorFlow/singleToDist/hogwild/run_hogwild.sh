#!/bin/bash
python hogwild.py --job_name "ps" --task_index 0 &
python hogwild.py --job_name "worker" --task_index 0 &
python hogwild.py --job_name "worker" --task_index 1 &

