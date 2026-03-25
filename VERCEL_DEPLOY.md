# Vercel 部署指南

## 快速部署

### 方法一：Vercel CLI（推荐）

```bash
# 1. 安装 Vercel CLI
npm install -g vercel

# 2. 登录 Vercel
vercel login

# 3. 部署到 preview 环境
vercel

# 4. 部署到 production 环境
vercel --prod
```

### 方法二：GitHub 集成

1. 将代码推送到 GitHub
2. 访问 [vercel.com](https://vercel.com)
3. 点击 "New Project"
4. 导入 GitHub 仓库
5. Vercel 会自动检测 VitePress 并配置
6. 点击 "Deploy"

## 项目配置

- **Framework**: VitePress
- **Build Command**: `npm run build`
- **Output Directory**: `docs/.vitepress/dist`
- **Install Command**: `npm install`

## 环境变量（如需要）

在 Vercel 项目设置中添加环境变量。

## 自定义域名

在 Vercel 项目设置中配置自定义域名。

## 预览部署

每次 push 到 GitHub 都会自动生成预览部署：
- `git push` → 自动创建 preview
- `git push --tags` → 自动创建 production

## 本地预览生产构建

```bash
npm run preview
```
