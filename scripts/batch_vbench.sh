#!/bin/bash

# List of video paths to be examined
special_video_paths=(
    "/home/yfeng/ygcheng/src/VideoSys/examples/open_sora_plan/outputs/29x480p_step50_search100_category/videos_vb900"
    "/home/yfeng/ygcheng/src/VideoSys/examples/open_sora_plan/outputs/29x480p_step70_search100_category/videos_vb900"
    "/home/yfeng/ygcheng/src/Open-Sora/samples/51x480p_step21"
    "/home/yfeng/ygcheng/src/Open-Sora/samples/51x480p_step15"
)

default_video_paths=(
    '/home/yfeng/ygcheng/src/VideoSys/outputs/sora_org_29x480p_vb900'
    '/home/yfeng/ygcheng/src/Open-Sora-Copy/samples/97x480p_step21_v6'
    '/home/yfeng/ygcheng/src/Open-Sora-Copy/samples/97x480p_step21_v7'
    '/home/hsliu/Open-Sora-raw/sample_deltadit/51480p_200'
    '/home/hsliu/Open-Sora-raw/sample_deltadit/97480p_200'
)

# JSON file paths
special_json_dir="/home/yfeng/ygcheng/src/VBench/vbench/VBench_full_info.json"
default_json_dir="/home/yfeng/ygcheng/src/VBench/prompts/vbench_200/extracted_prompts_200.json"

# Fixed argument for the evaluate.py script
dimension=""

# # Process video paths with the special JSON file
# echo "Processing video paths with special JSON file: $special_json_dir"
# for videos_path in "${special_video_paths[@]}"; do
#     echo "Processing videos in: $videos_path"
    
#     CUDA_VISIBLE_DEVICES=1 python evaluate.py \
#         --full_json_dir "$special_json_dir" \
#         --dimension "$dimension" \
#         --videos_path "$videos_path"
    
#     echo "Finished processing: $videos_path"
#     echo "----------------------------------------"
# done

# Process video paths with the default JSON file
echo "Processing video paths with default JSON file: $default_json_dir"
for videos_path in "${default_video_paths[@]}"; do
    echo "Processing videos in: $videos_path"
    
    CUDA_VISIBLE_DEVICES=3 python evaluate.py \
        --full_json_dir "$default_json_dir" \
        --dimension "$dimension" \
        --videos_path "$videos_path"
    
    echo "Finished processing: $videos_path"
    echo "----------------------------------------"
done

echo "All video paths have been processed."