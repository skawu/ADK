# ADK — AI Development Kit

ADK 是一套面向真实软件工程的、可复用的 AI 开发规范与技能套件。它将通用工程规则、技术栈规范、按需加载的 Skills、项目适配配置和可执行验证机制组织为独立版本化资产，供不同代码仓库复用。

## 目标

- 提高 AI 在既有工程中的理解、实现、调试、验证与交付质量。
- 降低需求误解、越界修改、未经验证即宣称完成、以及反复人工纠偏的发生率。
- 支持 Qt/QML、C++/CMake、Go、嵌入式与 MCU 等工程，并允许项目保留自己的架构与约束。
- 从实际工程中提炼通用实践，以可复现验证结果驱动迭代。

## 非目标

- ADK 不是 Agent 运行时、任务调度系统或模型服务。
- ADK 不替代项目自身的架构文档、测试、CI、安全政策或人工决策。
- ADK 不要求所有项目采用同一技术栈、目录结构、分支策略或阶段门。
- ADK 不把未经验证的经验直接升级为强制规则。

## 核心组成

1. **Core Rules**：工程事实优先、范围控制、安全边界、验证证据与交付要求。
2. **Skills**：通用工程工作流与 Qt/QML、C++、Go、嵌入式等技术专用流程。
3. **Technical Profiles**：技术栈相关的约束与检查点。
4. **Adapters**：将源内容映射到实际 AI 工具和项目注册机制；安装目标必须经核实。
5. **Checks & Evals**：结构检查与真实任务行为评估，两者分别记录。

## 文档导航

- [架构与职责边界](docs/architecture.md)
- [项目接入与升级](docs/adoption.md)
- [Skill 编写规范](docs/skill-authoring.md)
- [适配器与工具接入](adapters/README.md)
- [核心规则](core/rules/)
- [技术 Profiles](profiles/)
- [可复用模板](templates/)
- [Skills](skills/)
- [评估与回归用例](evals/README.md)

## 状态与版本

当前处于 v0.1 初始基线建设阶段。已有核心规则、技术 Profiles、模板、通用与技术专用 Skills、结构校验脚本和 CI。行为评估场景已定义，但尚不能视为已执行或通过。版本信息见 VERSION 与 CHANGELOG.md。

## 建设原则

- 通用规则与项目事实分离。
- 强制规则与按需技能分离。
- 文件存在与工具实际激活分离。
- 要求与验证证据分离。
- 尽可能自动检查可机器判定的要求。
- 优先使用最小、可审查、可回滚的变更。
- 保留清晰的变更记录和版本兼容说明。

## 本地校验

需要 Python 3.10 或更高版本，不需要安装第三方包：

- python -m unittest discover -s tests -v
- python scripts/validate_kit.py

CI 在 Pull Request 和推送时执行相同的检查。
