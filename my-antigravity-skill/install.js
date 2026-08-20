#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const SKILL_NAME = 'my-antigravity-skill';
const sourceDir = path.join(__dirname, 'skill-template');
const projectRoot = process.cwd();
const antigravityTargetDir = path.join(projectRoot, '.agents', 'skills', SKILL_NAME);

console.log(`Đang cài đặt skill "${SKILL_NAME}"...`);

// 1. Cài đặt cho Antigravity Agent
function copyDirectorySync(src, dest) {
    if (!fs.existsSync(dest)) {
        fs.mkdirSync(dest, { recursive: true });
    }
    const entries = fs.readdirSync(src, { withFileTypes: true });
    for (let entry of entries) {
        const srcPath = path.join(src, entry.name);
        const destPath = path.join(dest, entry.name);
        if (entry.isDirectory()) {
            copyDirectorySync(srcPath, destPath);
        } else {
            fs.copyFileSync(srcPath, destPath);
        }
    }
}

try {
    copyDirectorySync(sourceDir, antigravityTargetDir);
    console.log(`✅ Đã cài đặt cho Antigravity tại: ${antigravityTargetDir}`);

    // 2. Cài đặt cho Claude (Cursor, Claude Code, Cline, Windsurf...)
    // Đọc nội dung SKILL.md để đưa vào các file rules phổ biến của Claude
    const skillContentPath = path.join(sourceDir, 'SKILL.md');
    if (fs.existsSync(skillContentPath)) {
        let skillContent = fs.readFileSync(skillContentPath, 'utf8');
        
        // Bỏ phần YAML frontmatter (phần dành riêng cho Antigravity) để Claude không bị rối
        skillContent = skillContent.replace(/^---\n[\s\S]*?\n---\n/, '').trim();
        
        const claudeRuleText = `\n\n# Skill: ${SKILL_NAME}\n${skillContent}\n`;

        // Các file cấu hình phổ biến của hệ sinh thái Claude
        const claudeFiles = [
            '.cursorrules', // Cursor IDE
            'CLAUDE.md',    // Claude Code (CLI)
            '.clinerules',  // Roo Code / Cline
            '.windsurfrules' // Windsurf
        ];

        claudeFiles.forEach(file => {
            const filePath = path.join(projectRoot, file);
            // Nếu file đã tồn tại thì append vào, nếu chưa thì tạo mới
            if (fs.existsSync(filePath)) {
                const currentContent = fs.readFileSync(filePath, 'utf8');
                if (!currentContent.includes(`# Skill: ${SKILL_NAME}`)) {
                    fs.appendFileSync(filePath, claudeRuleText);
                    console.log(`✅ Đã thêm skill vào file ${file} cho Claude.`);
                } else {
                    console.log(`ℹ️ Skill đã tồn tại trong ${file}, bỏ qua.`);
                }
            } else {
                fs.writeFileSync(filePath, claudeRuleText);
                console.log(`✅ Đã tạo mới file ${file} cho Claude.`);
            }
        });
    }

    console.log(`🚀 Cài đặt hoàn tất! Skill của bạn giờ có thể hoạt động trên cả Antigravity và Claude!`);
} catch (error) {
    console.error(`❌ Lỗi khi cài đặt skill: ${error.message}`);
    process.exit(1);
}
