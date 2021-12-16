var app = new Vue({
    el: '#app',
    data: {
        theme: 'dark',
        switchThemeMessage: 'Turn off dark mode',
        file: null,
        numberPlate: '',
        isLoading: false,
        result: '',
        image: '',
        copyTooltip: 'copy'
    },
    methods: {
        switchTheme() {
            const theme = document.getElementById('theme');
            this.theme === 'dark' ? this.switchThemeMessage = 'Turn off dark mode' : this.switchThemeMessage = 'Turn on dark mode';
            this.theme === 'dark' ? this.theme = 'light' : this.theme = 'dark';
            theme.setAttribute('data-theme', this.theme);
        },
        onFileChange(e) {
            const files = e.target.files || e.dataTransfer.files;
            if (!files.length) return;
            this.file = files[0];
            this.image = URL.createObjectURL(files[0]);
        },
        async submit() {
            if (!this.file) return;
            this.isLoading = true
            const formData = new FormData();
            formData.append('file', this.file, this.file.name);
            const res = await fetch('/read-plate', {
                method: 'POST',
                redirect: 'follow',
                body: formData
            })
            this.result = await res.json();
            this.isLoading = false;
        },
        reset() {
            this.file = null;
            this.result = '';
            this.image = '';
            this.copyTooltip = 'copy';
        },
        copyPlate() {
            this.copyTooltip = 'copied';
            if (navigator.clipboard && window.isSecureContext) {
                return navigator.clipboard.writeText(this.result);
            } else {
                let textArea = document.createElement("textarea");
                textArea.value = this.result;

                textArea.style.position = "fixed";
                textArea.style.left = "-999999px";
                textArea.style.top = "-999999px";

                document.body.appendChild(textArea);

                textArea.focus();
                textArea.select();

                return new Promise((res, rej) => {
                    document.execCommand('copy') ? res() : rej();
                    textArea.remove();
                });
            }
        }
    }
})