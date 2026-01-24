import os

# Base directory for the collection
base_dir = r"C:\Users\Administrator\.claude\skills\claude-skills-collection"

# The Self-Evolution section to append
self_evolution_section = """
## 🧠 记忆与自进化 (Memory & Self-Evolution)

**1. 读取记忆**：
在开始任务前，**必须**读取 `memory/preferences.md`。这里保存了用户的个性化偏好、禁忌和习惯。请根据这些偏好调整你的工作方式。

**2. 接收反馈**：
任务完成后，如果用户提供了反馈（修改意见、批评或表扬）：
- **分析**：识别这是单次指令还是长期偏好。
- **记录**：如果是长期偏好，请立即使用 File Edit 工具将规则追加/更新到 `memory/preferences.md` 中。
- **确认**：告诉用户"已将此偏好记入我的长期记忆"。

**记忆文件位置**：`@path/memory/preferences.md`
"""

# List of skills to update
skills_to_update = [
    "ai-proofreading",
    "content-converter",
    "image-generator",
    "personal-knowledge-search",
    "superpowers",
    "topic-generator",
    "vibe-writer",
    "vibe-writer-pro"
]

def update_skill(skill_name):
    skill_path = os.path.join(base_dir, skill_name)
    skill_md_path = os.path.join(skill_path, "SKILL.md")
    memory_dir = os.path.join(skill_path, "memory")
    pref_file = os.path.join(memory_dir, "preferences.md")

    # 1. Create memory directory and preferences file if not exist
    if not os.path.exists(memory_dir):
        print(f"Creating memory directory for {skill_name}...")
        os.makedirs(memory_dir)
    
    if not os.path.exists(pref_file):
        print(f"Creating default preferences.md for {skill_name}...")
        with open(pref_file, "w", encoding="utf-8") as f:
            f.write(f"# User Preferences for {skill_name}\n\nThis file stores user preferences learned over time.\n")

    # 2. Check if SKILL.md exists
    if not os.path.exists(skill_md_path):
        print(f"Error: {skill_md_path} not found. Skipping.")
        return

    # 3. Read SKILL.md to check if already updated
    with open(skill_md_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "## 🧠 记忆与自进化" in content:
        print(f"{skill_name} already has self-evolution mechanism. Skipping update.")
    else:
        print(f"Updating {skill_name} with self-evolution mechanism...")
        with open(skill_md_path, "a", encoding="utf-8") as f:
            f.write(f"\n{self_evolution_section}")

if __name__ == "__main__":
    print(f"Starting batch update for {len(skills_to_update)} skills...")
    for skill in skills_to_update:
        try:
            update_skill(skill)
        except Exception as e:
            print(f"Failed to update {skill}: {e}")
    print("Batch update completed.")
