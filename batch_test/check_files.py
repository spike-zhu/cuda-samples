import os
def check_matching_files(root_dir, nums_of_success_build_cuda_samples, nums_of_unsuccess_build_cuda_samples):
    if not os.path.exists(root_dir):
        print(f"Error: directory {root_dir} does not exist")
        return
    
    total = 0
    for folder in sorted(os.listdir(root_dir)):
        folder_path = os.path.join(root_dir, folder)
        if os.path.isdir(folder_path): 
            for sub_folder in sorted(os.listdir(folder_path)):
                sub_folder_path = os.path.join(folder_path, sub_folder)
                if os.path.isdir(sub_folder_path):  
                    total += 1
                    expected_file_path = os.path.join(sub_folder_path, sub_folder)
                    if os.path.exists(expected_file_path):  # 检查是否有同名文件
                        print(f"[INFO] [{folder}] [{sub_folder}]  SUCCESS")
                        nums_of_success_build_cuda_samples +=1
                    else:
                        print(f"[INFO] [{folder}] [{sub_folder}]  FAILED")
                        nums_of_unsuccess_build_cuda_samples +=1
    print("[INFO] total_count_cuda_samples:", total)
    return nums_of_success_build_cuda_samples, nums_of_unsuccess_build_cuda_samples

if __name__ == "__main__":
    current_script_path = os.path.abspath(__file__)
    samples_directory = os.path.join(os.path.dirname(os.path.dirname(current_script_path)), "Samples")
    success_count = 0
    unsuccess_count = 0
    success_count, unsuccess_count = check_matching_files(samples_directory, success_count, unsuccess_count)
    print("[INFO] success_build_cuda_samples_count:", success_count)
    print("[INFO] failed_build_cuda_samples_count", unsuccess_count)

