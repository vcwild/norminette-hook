<div align="center">
    <img src=".github/assets/hook.svg" width="200px" />
    <div>
        <img src="https://img.shields.io/github/v/release/vcwild/norminette-hook?include_prereleases&color=%23FBC86D&style=flat-square" alt="release">
        <img src="https://img.shields.io/github/license/vcwild/norminette-hook?color=%23FBC86D&style=flat-square" alt="license" />
        <img src="https://img.shields.io/github/repo-size/vcwild/norminette-hook?color=%23FBC86D&style=flat-square" alt="repo size" />
    </div>
</div>

# Norminette Hook

The Norminette pre-commit hook.

## ❓ About

Git hooks are actions triggered whenever you do a commit.

After you execute a `git commit`, the **norminette-hook** will automatically trigger Norminette on your staged files, and if you are off the norm it will display what needs to be fixed before you can record this commit to your git history.

This ensures that every commit you do will follow the rules, and you don't have to run Norminette manually anymore.

By default, the Norminette hook will only check for files in **stage**, it is not running for every existing file of your project!

We realized that this is a better design, for you can write tests and other libraries that do not require strict rules.

## 📝 Requirements

- [Pre-commit](https://pre-commit.com/index.html) must be installed system-wide or in a virtual environment.

## 💿 Usage

Create a `.pre-commit-config.yaml` file in the root of your repository.

Add there the following lines:

```yaml
default_language_version:
  python: python3

repos:
  - repo: https://github.com/vcwild/norminette-hook
    rev: v0.1.1
    hooks:
    - id: norminette-hook
```

When executing `pre-commit run` or `pre-commit run norminette-hook`, the hook will be triggered.

Now install the hook to execute it automatically for each commit.

```bash
pre-commit install --install-hooks --overwrite
```

You are now ready for some next level linting automation! 👨‍🚀🚀

## 🙋 FAQ / Common issues <a name="faq"></a>

#### Error "bash: pre-commit: command not found"

Make sure you have installed [pre-commit](https://pre-commit.com/index.html) and it is available in the current shell environment.

#### How to commit without running Norminette?

If you want to skip commit hooks for whatever reason, simply use:

```sh
git commit --no-verify
```

#### How to remove this hook?

Simply remove the folder where pre-commit hooks is installed:

```sh
rm -f [root_dir]/.git/hooks/pre_commit`
```

This only removes the hook from executing after every commit. If you want to wipe your pre-commit installation, please follow [pre-commit uninstall](https://pre-commit.com/#pre-commit-uninstall)

## 🤝 Contributing

Fork the repository and create a pull request.

## 🏷️ License

The project is under the [MIT License](https://opensource.org/licenses/MIT). The software is provided as is, without warranty of any kind.
