class Commands:
    @staticmethod
    def publicArchive():
        colored_print("打包插件...")
        runcmd(
            "cd extension && make build && cd .. && zip -r release/extension_$(date '+%Y-%m-%d').zip extension/dist/*"
        )
