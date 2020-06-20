# Conditional build:
%bcond_with	slang		# use slang library instead of ncurses
%bcond_without	sasl		# don't use sasl
%bcond_with	gdbm		# use GDBM instead of BerkeleyDB
%bcond_with	qdbm		# use QDBM instead of BerkeleyDB
%bcond_with	tokyocabinet	# use TokyoCabinet instead of BerkeleyDB
#
%if %{without gdbm} && %{without qdbm} && %{without tokyocabinet}
%define	with_bdb	1
%endif
Summary:	The NeoMutt Mail User Agent
Summary(de.UTF-8):	Der NeoMutt Mail-User-Agent
Summary(es.UTF-8):	NeoMutt, cliente de correo electrónico
Summary(fr.UTF-8):	Agent courrier NeoMutt
Summary(ko.UTF-8):	텍스트 기반의 MUA
Summary(pl.UTF-8):	Program pocztowy NeoMutt
Summary(pt_BR.UTF-8):	NeoMutt, cliente de correio eletrônico
Summary(ru.UTF-8):	Почтовая клиентская программа NeoMutt
Summary(tr.UTF-8):	NeoMutt elektronik posta programı
Summary(uk.UTF-8):	Поштова клієнтська програма NeoMutt
Name:		neomutt
Version:	20200619
Release:	1
License:	GPL v2+
Group:		Applications/Mail
Source0:	https://github.com/neomutt/neomutt/archive/%{version}.tar.gz
# Source0-md5:	965111dd06dc060c84981d8b7eff46c7
Source1:	%{name}.desktop
URL:		http://www.mutt.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1.6
%{?with_sasl:BuildRequires:	cyrus-sasl-devel >= 2.1.0}
%{?with_bdb:BuildRequires:	db-devel >= 4.0}
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
%{?with_gdbm:BuildRequires:	gdbm-devel}
BuildRequires:	gettext-tools
BuildRequires:	gpgme-devel >= 1:1.1.1
BuildRequires:	libidn-devel
BuildRequires:	libxslt-progs
BuildRequires:	lynx
BuildRequires:	lz4-devel
%{!?with_slang:BuildRequires:	ncurses-devel >= 5.0}
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_qdbm:BuildRequires:	qdbm-devel}
%{?with_slang:BuildRequires:	slang-devel}
%{?with_tokyocabinet:BuildRequires:	tokyocabinet-devel}
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
Requires:	iconv
Suggests:	mailcap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	-fomit-frame-pointer

%description
NeoMutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

%description -l de.UTF-8
NeoMutt ist ein kleiner aber leistungsfähiger Vollbild-Mail-Client für
Unix mit MIME-Unterstützung, Farbe, POP3-Unterstützung,
Nachrichten-Threading, zuweisbaren Tasten und Sortieren nach Threads.

%description -l es.UTF-8
NeoMutt es un pequeño, pero muy potente cliente de correo en pantalla
llena. Incluye soporte a tipos MINE, color, POP3; encadenamiento de
mensajes, teclas configurables y clasificaciones por encadenamiento.

%description -l fr.UTF-8
mutt est un client courrier Unix plein écran, petit mais très
puissant. Il dispose de la gestion MIME, des couleurs, de la gestion
POP, des fils de discussion, des touches liées et d'un mode de tri sur
les fils.

%description -l ko.UTF-8
NeoMutt는 작지만 매우 강력한 텍스트 기반의 메일 클라이언트이다. NeoMutt는 많은 설정이 가능하다. 그리고, 키바인딩, 키보드
메크로, 메일 스레딩과 같은 진보된 형태와 정규표현식 검색, 메일에서 선택된 그룹의 내용에서 강력하게 일정한 패턴을 찾아내는
것을 지원함으로써 메일의 파워 유저에게 가장 적합하다.

%description -l pl.UTF-8
NeoMutt jest niewielkim programem pocztowym dla terminali tekstowych,
posiadającym duże możliwości. Obsługuje MIME, POP3, cztery formaty
skrzynek pocztowych, kolory, wątki, ocenę ważności listów (scoring)
oraz skompresowane foldery.

%description -l pt_BR.UTF-8
O NeoMutt é um pequeno mas muito poderoso cliente de correio em tela
cheia. Inclui suporte a tipos MIME, cor, POP3, encadeamento de
mensagens, teclas configuráveis e classificação por encadeamento.

%description -l ru.UTF-8
NeoMutt - это небольшой, но мощный полноэкранный почтовый клиент.
Включает поддержку MIME, цвет, поддержку POP3 и IMAP, группировку
сообщений по цепочкам, переопределяемые клавиши, поддержку pgp/gpg и
сортировку сообщений в цепочках. Включает также (пока что
экспериментальную) поддержку NNTP.

%description -l tr.UTF-8
NeoMutt, küçük ama çok güçlü bir tam-ekran Unix mektup istemcisidir. MIME
desteği, renk ve POP3 desteği içerir.

%description -l uk.UTF-8
NeoMutt - це невеликий, але потужний повноекранний поштовий клієнт.
Містить підтримку MIME, колір, підтримку POP3 та IMAP, групування
повідомлень по ланцюжкам, перевизначення клавіш, підтримку pgp/gpg та
сортування повідомлень у ланцюжках. Містить також (поки що
експериментальну) підтримку NNTP.

%prep
%setup -q

%build
./configure \
	LDFLAGS="${LDFLAGS:-%rpmldflags}" \
	CFLAGS="${CFLAGS:-%rpmcflags}" \
	CXXFLAGS="${CXXFLAGS:-%rpmcxxflags}" \
	FFLAGS="${FFLAGS:-%rpmcflags}" \
	FCFLAGS="${FCFLAGS:-%rpmcflags}" \
	CPPFLAGS="${CPPFLAGS:-%rpmcppflags}" \
	%{?__cc:CC="%{__cc}"} \
	%{?__cxx:CXX="%{__cxx}"} \
	--host=%{_target_platform} \
	--build=%{_target_platform} \
	--prefix=%{_prefix} \
	%{!?debug:--disable-debug} %{?debug:--enable-debug} \
	--gpgme \
	%{?with_bdb:--bdb --with-bdb=/usr} \
	%{!?with_slang:--with-ui=ncurses} \
	%{?with_gdbm:--gdbm} \
	--lz4 \
	--with-mailpath=/var/mail \
	--mixmaster \
	%{?with_qdbm:--qdbm} \
	%{?with_sasl:--sasl} \
	%{?with_slang:--with-ui=slang} \
	--ssl \
	%{?with_tokyocabinet:--tokyocabinet} \
	--zlib \
	--zstd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_mandir}/pl/man1} \
	$RPM_BUILD_ROOT%{_sysconfdir}/NeoMuttrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	DOTLOCK_GROUP=

install contrib/gpg.rc $RPM_BUILD_ROOT%{_sysconfdir}/NeoMuttrc.d
install contrib/smime.rc $RPM_BUILD_ROOT%{_sysconfdir}/NeoMuttrc.d
install contrib/colors.linux $RPM_BUILD_ROOT%{_sysconfdir}/NeoMuttrc.d/colors.rc
install contrib/logo/neomutt-64.png $RPM_BUILD_ROOT%{_pixmapsdir}/neomutt.png

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

cat <<'EOF' >$RPM_BUILD_ROOT%{_bindir}/neomutt_source-neomuttrc.d
#!/bin/sh -e
for rc in %{_sysconfdir}/NeoMuttrc.d/*.rc; do
	[ ! -r "$rc" ] || echo "source \"$rc\""
done
EOF

# keep manual.txt.gz, the rest is installed as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}/[!m]*

%find_lang neomutt

%clean
rm -rf $RPM_BUILD_ROOT

%files -f neomutt.lang
%defattr(644,root,root,755)
%doc contrib/{*rc*,*cap*} ChangeLog.md README.md
%dir %{_sysconfdir}/NeoMuttrc.d
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/neomuttrc
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/NeoMuttrc.d/*.rc
%attr(755,root,root) %{_bindir}/neomutt
%attr(755,root,root) %{_bindir}/neomutt_source-neomuttrc.d
%dir %{_libexecdir}/%{name}
%attr(755,root,root) %{_libexecdir}/%{name}/pgpewrap
%attr(755,root,root) %{_libexecdir}/%{name}/smime_keys

%{_docdir}/%{name}
%{_desktopdir}/neomutt.desktop
%{_pixmapsdir}/neomutt.png
%{_mandir}/man1/neomutt.1*
%{_mandir}/man1/pgpewrap_neomutt.1*
%{_mandir}/man1/smime_keys_neomutt.1*
%{_mandir}/man5/mbox_neomutt.5*
%{_mandir}/man5/mmdf_neomutt.5*
%{_mandir}/man5/neomuttrc.5*
