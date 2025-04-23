#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# set the cuda-samples build directory and log file path
SAMPLES_DIR="$SCRIPT_DIR/../Samples"
LOG_FILE="$SCRIPT_DIR/test_cuda_samples.log"

# record cuda-samples result in log file
exec > >(tee -a "$LOG_FILE") 2>&1

# make sure cuda-samples directory exist
if [ ! -d "$SAMPLES_DIR" ]; then
    echo "Error: Samples directory does not exist."
    exit 1
fi

category_index=0

# execute make build
for category_dir in "$SAMPLES_DIR"/*; do
    if [ -d "$category_dir" ]; then
        echo "[INFO] Processing category #$category_index: $category_dir"
        cd "$category_dir"
        project_index=0
        for project_dir in */; do
            if [ -d "$project_dir" ]; then
                echo "[INFO] Processing project #[$category_index]-[$project_index]: $project_dir"
                cd "$project_dir"
                echo "[INFO] Building in $(pwd)"
                make SMS="80" NVCCFLAGS="-lstdc++ -lm"
                # make clean
                cd ..
                project_index=$((project_index + 1))
                echo
            fi
        done
        cd .
        category_index=$((category_index + 1))
    fi
done

echo "[INFO] All projects have been built." | tee -a "$LOG_FILE"

